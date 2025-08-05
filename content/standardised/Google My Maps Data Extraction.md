---
aliases: 
category: 
date modified: 1-08-2025
tags:
  - devops
---
### Summary:

This guide covers the key workflows and tools for managing and processing location data in Google Sheets and Google My Maps. Suppose we have marks on Google My Maps. In order to extract the location of markers to a google sheet.

1. **Export Marker Data** from Google My Maps as KML/CSV.
2. Convert KML to CSV
3. **Use Apps Script in Google Sheets** to extract data like addresses or postal codes from coordinates.

### **Extract Data from Google My Maps**  
   - **Export Custom Markers:**
     1. Open Google My Maps.
     2. Use the menu (three dots) to select **Export to KML**.
     3. The exported file will contain marker names, descriptions.

### Extract KML data to google sheets
   
- Rename KML file to XML.
- Open XML in excel.
- Extract marker and coordinate data.
- Paste data into google sheets.

### **Extracting Information from Coordinates in Google Sheets**  

Use [[**Google Apps Script**]] to extract additional information like addresses or postal codes from geographic coordinates.

- **Get Address from Coordinates**:
  ```javascript
  function getAddress(lat, lng) {
    var response = Maps.newGeocoder().reverseGeocode(lat, lng);
    var result = response.results[0];
    if (result) {
      return result.formatted_address;
    } else {
      return 'No address found';
    }
  }
  ```
- **Get Postal Code from Coordinates**:
  ```javascript
  function getPostalCode(lat, lng) {
    var response = Maps.newGeocoder().reverseGeocode(lat, lng);
    var result = response.results[0];
    if (result) {
      for (var i = 0; i < result.address_components.length; i++) {
        var component = result.address_components[i];
        if (component.types.indexOf('postal_code') !== -1) {
          return component.long_name;
        }
      }
      return 'Postal code not found';
    } else {
      return 'No results found';
    }
  }
  ```
- Use `getAddress()` with `getPostalCode()`.
- =getPostalCode(56.033139, -3.4182519)


