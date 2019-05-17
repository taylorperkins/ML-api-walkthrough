# API Spec

## Requirements

* **Add an endpoint we can HTTP POST a flower species prediction request to.**

## Guidelines

* **All successful calls should return HTTP code 200.**


## API Request

**CONTENT TYPE: application/json**

**HTTP METHOD: POST**

### Request Schema:
```
{
  "FlowerPredictionRequestSchema": {
    "type": "object",
    "required": [
      "FlowerID",
      "PetalLength",
      "PetalWidth",
      "SepalLength",
      "SepalWidth"
    ],
    "properties": {
      "FlowerID": {
        "title": "FlowerID",
        "type": "number",
        "format": "integer"
      },
      "PetalLength": {
        "title": "PetalLength",
        "type": "number",
        "format": "decimal"
      },
      "PetalWidth": {
        "title": "PetalWidth",
        "type": "number",
        "format": "decimal"
      },
      "SepalLength": {
        "title": "SepalLength",
        "type": "number",
        "format": "decimal"
      },
      "SepalWidth": {
        "title": "SepalWidth",
        "type": "number",
        "format": "decimal"
      }
    }
  }
}
```

#### Sample Request:
```
{
  "FlowerID": 1,
  "SepalLength": 4.9,
  "SepalWidth": 2.5,
  "PetalLength": 4.5,
  "PetalWidth": 1.7
}
```

### Response Schema:
```
{
  "FlowerPredictionResponseSchema": {
    "properties": {
      "FlowerID": {
        "title": "FlowerID",
        "type": "number",
        "format": "integer"
      },
      "Species": {
        "title": "Species",
        "type": "string"
      }
    },
    "type": "object",
    "required": [
      "FlowerID",
      "Species"
    ]
  }
}

```

#### Sample Response:
```
{
  "FlowerID": 1,
  "Species:": "versicolor"
}
```