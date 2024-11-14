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
  "session": "string glaub ich aber da bist du der itsi experte falls passt sonst infos",
  "info": "string"
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
  "session": "string",
  "info": "string"
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
      "string",
      "string"
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
    "favouritesOnly": false
  }
}
```

### Response

```json
{
  "images": [
    {
      "id": "string",
      "header": "string",
      "description": "string",
      "date": "string",
      "tags": [
        "string",
        "string"
      ],
      "url_preview": "string",
      "url_full": "string",
      "camera": "string",
      "favourite": true
    },
    {
      
    }
  ]
}
```

## Camera
`api.wildeye.tech/camera`

### Post /all
`/camera/all`

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
      "info":[
        "camera",
        "night vision"
      ],
      "name": "string",
      "id": 1,
      "description": "string",
      "lastCapturePreview": "string",
      "lastCaptureDate": "string",
      "totalCaptures": 10,
      "battery": 100,
      "status": "online | offline",
      "lastSync": "string",
      "preferences": {
        "favourite": true
      }
    },
    {
      
    }
  ]
}
```

### Post /certain

`camera/certain`

```json
{
  "session": "string",
  "ids": [
    1,
    2
  ]
}
```

### Response

```json
{
  "cameras": [
    {
      "lat": 48.4262157636489,
      "lng": 16.61251026756385,
      "info":[
        "camera",
        "night vision"
      ],
      "name": "string",
      "id": 1,
      "description": "string",
      "lastCapturePreview": "string",
      "lastCaptureDate": "string",
      "totalCaptures": 10,
      "battery": 100,
      "status": "online | offline",
      "lastSync": "string",
      "preferences": {
        "favourite": true
      }
    },
    {
      
    }
  ]
}
```
