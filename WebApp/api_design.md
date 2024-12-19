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
    "heartedOnly": false
  }
}
```

### Response

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
      "url_preview": "string",
      "url_full": "string",
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
      "generalInfo": "string",
      "name": "string",
      "id": 1, 
      "lastCapturePreview": "url/string",
      "lastCaptureDate": "string",
      "totalCaptures": 10,
      "battery": 100,
      "lastSync": "string",
      "hearted": true
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
      "generalInfo": "string",
      "name": "string",
      "id": 1,
      "lastCapturePreview": "url/string",
      "lastCaptureDate": "string",
      "totalCaptures": 10,
      "battery": 100,
      "lastSync": "string",
      "hearted": true
    },
    {
      
    }
  ]
}
```

### Post /advancedSettings

```json
{
  "session": "string",
  "id": 1
}
```

### Response 
Beispiel für Number, String, Boolean und Select inputs von leos liste auf github
```json
[
{
  "type": "number", 
  "name": "Resolution",
  "min": 0,
  "max": 100,
  "value": 50,
  "required": true
},
{
  "type": "string",
  "name": "prefix",
  "value": "WildEye",
  "required": false
},
{
  "type": "boolean",
  "name": "Nightvision",
  "value": true,
  "required": true
},
{
  "type": "select",
  "name": "Logging",
  "options": ["None", "Error", "Warning", "Info", "Debug"],
  "value": "Info",
  "required": true
}
]
```

### Put /advancedSettings

```json
{
  "session": "string",
  "id": 1,
  "advancedSettings": [
    {
      "type": "number",
      "name": "Resolution",
      "min": 0,
      "max": 100,
      "value": 50,
      "required": true
    },
    {
      "type": "string",
      "name": "prefix",
      "value": "WildEye",
      "required": false
    },
    {
      "type": "boolean",
      "name": "Nightvision",
      "value": true,
      "required": true
    },
    {
      "type": "select",
      "name": "Logging",
      "options": ["None", "Error", "Warning", "Info", "Debug"],
      "value": "Info",
      "required": true
    }
  ]
}
```

### Response

```json
{
  "success": "boolean"
}
```