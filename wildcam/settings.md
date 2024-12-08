# Settings

## General

### Data Protection 

discardRecordingsIfHumanDetected: bool

### Data Collection

collectEnvironmentData: bool
collectGyroscopeData: bool
collectGPSData: bool
collectDetectionData: bool

### Logging

logLevel: str

### Space Management

overrideDataIfFull: bool

## Detection

detectionTimeout: int
(detectionTimeoutDay: int)
(detectionTimeoutNight: int)

### PIR Sensor

pirSensitivity: int

### Double Check (Optional)

opticalFlow: bool

## Recording

recordType: str
setTimeBasedRecording: bool
setIntervalBasedRecording: bool

### Image

imageQuality: int
burstAmount: int
burstInterval: int

### Video

videoQuality: int
videoLength: int

## Update Cycle

### Trigger

updateTrigger: str  (amount, interval, both)
recordAmount: int
updateInterval: int

### Message

(Thresholds used to determine a change)
notifyOnGyroChange: bool
notifyOnGPSChange: bool
sendLogs: bool

## Transmission

transmissionRetryAmount: int
