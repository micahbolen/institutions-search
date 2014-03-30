"""a simple webapp2 server."""

import webapp2

import csv 
import json


class MainPage(webapp2.RequestHandler):

    def get(self):
    	q = self.request.get('q')
        json_data=open('institutions.json')

        data = json.load(json_data)
        results = []
        for row in data:
            if q.lower() in row["name"].lower():
                results.append(row["name"]) 

        self.response.write(json.dumps(results))
        json_data.close()       	

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
