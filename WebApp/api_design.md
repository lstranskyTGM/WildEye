# API Design

*13.11.2024 v1.01*

## Register
`api.wildeye.tech/register`

### Post

```json
{
  "username": "string",
  "password": "string halt gehashed unf gesalted fallst du das willst",
  "email": "string"
}
```

### Response

```json
{
  "session": "string glaub ich aber da bist du der itsi experte falls passt sonst infos"
}
```

## Login
`api.wildeye.tech/login`
### Post

```json
{
  "username": "string",
  "password": "string halt gehashed unf gesalted fallst du das willst"
}
```

### Response

```json
{
  "session": "string"
}
```

## Logout
`api.wildeye.tech/logout`
### Post

```json
{
  "session": "string"
}
```

### Response

```json
{
  "success": true
}
```

## Pictures
`api.wildeye.tech/pictures`
### Get

```json
{
  "session": "string",
  "settings": {
    "cameras": [
      "id",
      "id"
    ],
    "sort": {
      "by": "date | name",
      "order": "asc | desc"
    },
    "pageLimit": 10,
    "page": 1,
    "search": "string",
    "date": {
      "from": "string",
      "to": "string"
    },
    "heartedOnly": false
  }
}
```

### Response

Welche Tags mit welchen Klassen übereinstimmen muss mit Julian abgeklärt werden, 
je nachdem, was seine AI halt kann. Es gibt auf jeden fall einen Tag mit dem Namen der Camera.

```json
{
  "images": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "date": "string",
      "tags": [
        {
          "title": "string",
          "icon": "bi bi-heart-fill"
        },
        {
          "title": "string",
          "icon": "bi bi-heart-fill"
        }
      ],
      "url": "string",
      "alt": "string",
      "camera": "string",
      "hearted": true
    },
    {
      
    }
  ]
}
```

## Camera
`api.wildeye.tech/camera`

### Post /cameras
`/cameras`

alle Cameras von dem Account werden zurückgegeben

```json
{
  "session": "string"
}
```

### Response

```json
{
  "cameras": [
    {
      "lat": 48.4262157636489,
      "lng": 16.61251026756385,
      "info": "string",
      "name": "string",
      "id": 1, 
      "lastCapturePreview": "url/string",
      "lastCaptureDate": "string",
      "totalCaptures": 10,
      "battery": 100,
      "lastSync": "string",
      "hearted": true
    }
  ]
}
```

### Post /camera/<int:id>

`camera/certain`

Nur die Kamera mit der ID wird zurückgegeben. Ich weiß nicht warum ich das mit einem url parameter
gemacht habe, falls ich es ändern soll bitte sagen.

```json
{
  "session": "string"
}
```

### Response

```json
{
  "cameras": [
    {
      "lat": 48.4262157636489,
      "lng": 16.61251026756385,
      "info": "string",
      "name": "string",
      "id": 1,
      "lastCapturePreview": "url/string",
      "lastCaptureDate": "string",
      "totalCaptures": 10,
      "battery": 100,
      "lastSync": "string",
      "hearted": true
    }
  ]
}
```

### Post /advancedSettings

Wenn die Settings für jede Kamera gleich sind, dann kann man die id auch weglassen.

```json
{
  "session": "string",
  "id": 1
}
```

### Response 
Beispiel für Number, String, Boolean und Select inputs von leos liste auf github.
Auf dem flask server hab ich das schon in json umgewandelt, und so erwarte ich es mir auch.
```json
[
  {
    "sectionName": "General",
    "sectionSettings": [
      {
        "type": "boolean",
        "name": "discardHumanRecordings",
        "value": true,
        "required": true
      },
      {
        "type": "boolean",
        "name": "collectGPSData",
        "value": true,
        "required": true
      }
    ]
  },
  {
    "sectionName": "Detection",
    "sectionSettings": [
      {
        "type": "number",
        "name": "defaultDetectionTimeout",
        "min": 0,
        "max": null,
        "value": 10,
        "required": true
      },
      {
        "type": "number",
        "name": "dayDetectionTimeout",
        "min": 0,
        "max": null,
        "value": 10,
        "required": false
      }
    ]
  }
]
```

### Put /advancedSettings
 
Nur der teil der sich wirklich verändert wird hier gegeben.
man kann hier eig auf alles bis auf name und value verzichten, aner es ist aufwand das zu machen

```json
[
  {
    "sectionName": "Detection",
    "sectionSettings": [
      {
        "type": "number",
        "name": "defaultDetectionTimeout",
        "min": 0,
        "max": null,
        "value": 10,
        "required": true
      }
    ]
  }
]
```

### Response

```json
{
  "success": "boolean"
}
```


## imageSearchSettings

### post

```json
{
  "session": "string"
}
```

### Response

```json
[
  {
    "sectionName": "General Search",
    "sectionSettings": [
      {
        "type": "string",
        "name": "Search for Names or Tags",
        "value": "",
        "required": false
      }
    ]
  },
  {
    "sectionName": "Cameras",
    "sectionSettings": [
      {
        "type": "boolean",
        "name": "string",
        "value": true,
        "required": true
      }
    ]
  }
]
```

## Images

### Post /imageSearch

```json
{
  "session": "string",
  "imageSearchSettings": "string, einfach das gleiche wie man bekommt von dem server",
  "page": 0
}
```

### Response

```json
[
  {
    "id": 0,
    "url": "https://www.w3schools.com/w3images/lights.jpg",
    "cameraID": 1,
    "alt": "Lights",
    "title": "Lights",
    "description": "Wunderschönes Bild",
    "date": "2021-09-01",
    "hearted": false,
    "tags": [
      {"icon": "bi bi-person", "text": "Person"},
      {"icon": "bi bi-camera", "text": "Camera"}
    ]
  },
  {
    "id": 1,
    "url": "https://www.w3schools.com/w3images/lights.jpg",
    "cameraName": 2,
    "alt": "Lights",
    "title": "Lights",
    "date": "2021-09-01",
    "hearted": false,
    "tags": [
      {"icon": "bi bi-person", "text": "Person"},
      {"icon": "bi bi-camera", "text": "Camera"},
      {"icon": "bi bi-camera", "text": "Camera"},
      {"icon": "bi bi-camera", "text": "Camera"},
      {"icon": "bi bi-camera", "text": "Camera"},
      {"icon": "bi bi-camera", "text": "Camera"},
      {"icon": "bi bi-camera", "text": "Camera"}

    ]
  }
]
```

## checkSession

### Post /checkSession

```json
{
  "session": "string"
}
```

### Response

```json
{
  "success": "True", 
  "authorized": "False"
}
```
