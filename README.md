# shopping-tracker

This project aims to scrape daily deals from 3 major Turkish e-shopping platform with the information scheme below with the aim of stock tracking to create new trade oppurtunities. Data stores on Amazon DynamoDB with the index of urls.

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
