import robotpy_apriltag
from wpimath.geometry import Transform3d

import photonvision


def test_photon_pose_estimator_ctor():
    camera = photonvision.PhotonCamera("test_ctor")
    estimator = photonvision.PhotonPoseEstimator(
        robotpy_apriltag.loadAprilTagLayoutField(
            robotpy_apriltag.AprilTagField.k2023ChargedUp
        ),
        photonvision.PoseStrategy.AVERAGE_BEST_TARGETS,
        camera,
        Transform3d(),
    )
    assert estimator
