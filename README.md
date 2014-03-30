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

A JSON array of results.

**Tech**

-  Python
-  JSON
-  Google App Engine
