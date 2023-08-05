import enum
import logging
import uuid

import numpy as np
import qi
from cltl.naoqi.api.camera import Image, Bounds, CameraResolution
from cltl.naoqi.spi.image import ImageSource
import vision_definitions

logger = logging.getLogger(__name__)


# See http://doc.aldebaran.com/2-5/naoqi/vision/alvideodevice.html?highlight=alvideodevice
class NAOqiCameraIndex(enum.IntEnum):
    TOP = 0
    BOTTOM = 1
    DEPTH = 2


RESOLUTION_CODE = {
    CameraResolution.NATIVE:    2,
    CameraResolution.QQQQVGA:   8,
    CameraResolution.QQQVGA:    7,
    CameraResolution.QQVGA:     0,
    CameraResolution.QVGA:      1,
    CameraResolution.VGA:       2,
    CameraResolution.VGA4:      3,
}

COLOR_SPACE = {
    'kYuv': 0, 'kyUv': 1, 'kyuV': 2,
    'Rgb':  3, 'rGb':  4, 'rgB': 5,
    'Hsy':  6, 'hSy':  7, 'hsY': 8,

    'YUV422': 9,  # (Native Color)

    'YUV': 10, 'RGB': 11, 'HSY': 12,
    'BGR': 13, 'YYCbCr': 14,
    'H2RGB': 15, 'HSMixed': 16,

    'Depth': 17,        # uint16    - corrected distance from image plan (mm)
    'XYZ': 19,          # 3float32  - voxel xyz
    'Distance': 21,     # uint16    - distance from camera (mm)
    'RawDepth': 23,     # uint16    - distance from image plan (mm)
}

SERVICE_VIDEO = "ALVideoDevice"
SERVICE_MOTION = "ALMotion"

# Only take non-blurry pictures
HEAD_DELTA_THRESHOLD = 0.1


class NAOqiCamera(object):
    def __init__(self, session, resolution, rate):
        # type: (qi.Session, CameraResolution, int) -> None
        """
        Initialize NAOqi Camera.

        More information on paramters can be found at:
        http://doc.aldebaran.com/2-1/naoqi/vision/alvideodevice.html

        Parameters
        ----------
        session: qi.Session
            NAOqi Application Session
        resolution: CameraResolution
            NAOqi Camera Resolution
        index: int
            Which NAOqi Camera to use
        """
        self._session = session

        self._color_space = COLOR_SPACE['YUV422']
        self._color_space_3D = COLOR_SPACE['Distance']

        self._resolution = resolution
        self._resolution_3D = resolution

        self._rate = rate

        self._service = None
        self._motion = None
        self._client = None

    def __enter__(self):
        # Register a Generic Video Module
        resolution = vision_definitions.kQQVGA
        colorSpace = vision_definitions.kYUVColorSpace
        fps = 20
        # TODO Check hasDepthCamera
        logger.info("NAOqiCamera started")

        return NAOqiImageSource(self._session,
                                self._client,
                                self._motion,
                                self._resolution,
                                self._rate,
                                self._color_space,
                                self._color_space_3D)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._service.unsubscribe(self._client)
        self._service = None
        self._motion = None
        self._client = None


class NAOqiImageSource(ImageSource):
    def __init__(self, service, client, motion, resolution, rate, color_space, color_space_3D):
        # type: (qi.Service, qi.Service, CameraResolution, int, int, int) -> None
        self._color_space = color_space
        self._color_space_3D = color_space_3D

        self._resolution = resolution
        self._resolution_3D = resolution

        self._rate = rate

        self._service = service
        self._client = client
        self._motion = motion

    @property
    def resolution(self):
        return self._resolution

    def capture(self):
        image_rgb, image_3D, view = None, None, None

        video_service = self._service.service("ALVideoDevice")

        # Register a Generic Video Module
        resolution = vision_definitions.kQQVGA
        colorSpace = vision_definitions.kRGBColorSpace
        fps = 20

        nameId = video_service.subscribe("python_GVM", resolution, colorSpace, fps)

        image = video_service.getImageRemote(nameId)

	video_service.unsubscribe(nameId)

        # TODO: RGB and Depth Images are not perfectly synced, can they?
        width, height, _, _, _, _, data, camera, left, top, right, bottom = image

	print(width, height)
        image_rgb = self._yuv2rgb(width, height, data)

        # Calculate Image Bounds in Radians
        # Apply Yaw and Pitch to Image Bounds
        # Bring Theta from [-PI/2,+PI/2] to [0, PI] Space
        phi_min, phi_max = right, left
        theta_min, theta_max = np.pi / 2, np.pi / 2
        view = Bounds(phi_min, theta_min, phi_max, theta_max)

        return Image(image_rgb, view, image_3D) if image_rgb is not None and view is not None else None

    def _yuv2rgb(self, width, height, data):
        # type: (int, int, bytes) -> np.ndarray
        """
        Convert from YUV422 to RGB Color Space

        Parameters
        ----------
        width: int
            Image Width
        height: int
            Image Height
        data: bytes
            Image Data

        Returns
        -------
        image_rgb: np.ndarray
        """

        X2 = width // 2
        if True:
            return  np.frombuffer(data, np.uint8).reshape(height, width, 3)

        RGB = np.empty((height, X2, 2, 3), np.float32)
        RGB[:, :, 0, :] = YUV442[..., 0].reshape(height, X2, 1)
        RGB[:, :, 1, :] = YUV442[..., 2].reshape(height, X2, 1)

        Cr = (YUV442[..., 1].astype(np.float32) - 128.0).reshape(height, X2, 1)
        Cb = (YUV442[..., 3].astype(np.float32) - 128.0).reshape(height, X2, 1)

        RGB[..., 0] += np.float32(1.402) * Cb
        RGB[..., 1] += - np.float32(0.71414) * Cb - np.float32(0.34414) * Cr
        RGB[..., 2] += np.float32(1.772) * Cr

        return RGB.clip(0, 255).astype(np.uint8).reshape(height, width, 3)

    def YUV2RGB(self, yuv):

        m = np.array([[ 1.0, 1.0, 1.0],
                     [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                     [ 1.4019975662231445, -0.7141380310058594 , 0.00001542569043522235] ])

        rgb = np.dot(yuv,m)
        rgb[:,:,0]-=179.45477266423404
        rgb[:,:,1]+=135.45870971679688
        rgb[:,:,2]-=226.8183044444304
        return rgb
