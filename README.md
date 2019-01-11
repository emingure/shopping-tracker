# shopping-tracker

This project aims to scrape daily deals from major Turkish e-shopping with the information scheme below. Data stores on Amazon DynamoDB with the index of urls.

```
{   
    'timestamp': "datetime",
    'productId': "string",
    'url': "string",
    'name': "string",
    'brand': "string",
    'definition': "string",
    'seller': "string",
    'price': "string",
    'originalPrice': "string",
    'listings': [
      {
        'store': "string",
        'price': "string",
        'url': "string",
        'stock': "string"
      },
      ...
    ],
    'stock': "string" 
}
```
