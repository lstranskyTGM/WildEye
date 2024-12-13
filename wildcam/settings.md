# Settings

## General

### Data Protection 

`discardHumanRecordings: bool`

### Data Collection

`collectEnvironmentData: bool`

`collectGyroscopeData: bool`

`collectGPSData: bool`

`collectDetectionData: bool`

### Logging

`logLevel: enum.Enum("DEBUG", "INFO", "WARNING", "ERROR")`

### Space Management

`overwriteOnFull: bool`

## Detection

### Timeouts

`defaultDetectionTimeout: int`

`(dayDetectionTimeout: int)`

`(nightDetectionTimeout: int)`

### PIR Sensor

`pirSensitivity: int(0-100)`

### Double Check (Optional)

`opticalFlow: bool`

## Recording

### Recording Type

`recordType: enum.Enum("PHOTO", "VIDEO", "BOTH")`

### Recording Triggers

`enableTrigger: bool`

`enableTimeSpan: bool`

`enableInterval: bool`

### Optional Parameters

`timeSpanStart: datetime.time`

`timeSpanEnd: datetime.time`

`intervalDurationSeconds: int`

### Image

`imageResolution: str`

`burstAmount: int`

`burstIntervalMilliseconds: int`

### Video

`videoResolution: int`

`videoLengthSeconds: int`

## Update Cycle

### Trigger

#### Amount-Based Trigger

`enableAmountTrigger: bool`

`recordAmountForUpdate: int`

#### Interval-Based Trigger

`enableIntervalTrigger: bool`

`updateIntervalMinutes: int`

### Message

(Thresholds used to determine a change)

`notifyOnGyroscopeChange: bool`

`notifyOnGPSChange: bool`

`logTransmissionLevel: enum.Enum("NONE", "ERROR", "WARNING", "INFO", "DEBUG")`

## Transmission

### Retry Policy

`transmissionRetries: int`
