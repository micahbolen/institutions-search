institutions-search
===================

Search for a U.S. college or university by name.

[Demo](http://institutions-search.appspot.com/?q=florida)

**Resource URL**

http://institutions-search.appspot.com

**Request Type**

GET

**Parameters**

q (optional) - Returns an array of school names that contain the value of this paramter.  Values are lowercased before comparison.  If no match is found, returns an empty array.   If parameter is not specified (or parameter is empty), all U.S. colleges and universities are returned.  

**Response Type**

JSON

**Example**

GET http://institutions-search.appspot.com/?q=fresno

Returns:

    ["California State University-Fresno", "Fresno City College", "Fresno Pacific University", "Heald College-Fresno", "San Joaquin Valley College-Fresno", "San Joaquin Valley College-Fresno Aviation", "Kaplan College-Fresno"]

**Tech**

-  Python
-  JSON
-  Google App Engine
