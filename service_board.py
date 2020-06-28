# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:27:30 2018

@author: James
"""

import ldbws_client

class train_obj:
    """
    Chooo Choo!
    """
    def __init__(self, origin, destination, platform, 
                 est_dept, sch_dept, calling_stops):
    
        self.origin = origin
        self.destination = destination
        self.platform = platform
        self.sch_dept = sch_dept
        self.est_dept = est_dept
        self.calling_stops = calling_stops
        
        
    def __repr__(self):
        string = '<train_obj: Origin: ' + self.origin + '\nDestination: '\
                  + self.destination + '\nPlatform: ' + self.platform + \
                  '\nScheduled departure: ' + self.sch_dept + '\nEstimated departure: ' \
                  + self.est_dept
                  
        string += '\nCalling stops:\n'
        for calling_stop in self.calling_stops:
            string += str(calling_stop) + '\n'
        string = string[:-1] + ' >'
                      
        return string
        

class calling_stop(object):
    """
    Simple structure to represent a calling stop
    """
    def __init__(self, location, sch_stop, est_stop):
        self.location = location
        self.sch_stop = sch_stop
        self.est_stop = est_stop
        
    def __repr__(self):
        string = '<calling_stop: Location: ' + self.location + ' Scheduled time: ' \
        + self.sch_stop + ' Estimated time: ' + self.est_stop + '>'
        return string
    

class service_board(object):
    """
    Class to hold info I need
    """
    def __init__(self, key):
        self.client = ldbws_client.ldbws_client(key)
        
    
    def get_services(self, crc, num_rows = 10):
        """
        Returns dictionary of trains
        """
        data = self.client.get_dep_board_with_details(num_rows, crc)
        train_services = data.trainServices
        self.trains = {}
        i = 0
        for train in train_services.service:
            origin = self.get_origin(train)
            destination = self.get_destination(train)
            platform = self.get_platform(train)
            sch_dept = self.get_sch_dept(train)
            est_dept = self.get_est_dept(train)
            calling_stops = self.get_calling_stops(train)
            
            self.trains[i] = train_obj(origin, destination, platform,
                                       est_dept, sch_dept, calling_stops)
            i += 1
            
        return self.trains
        
    
    def get_est_dept(self, train):
        """Extract the estimated departure time attribute from the train object"""
        try:
            return train.etd
        except AttributeError:
            return ''
        
    def get_origin(self, train):
        """Extract the origin attribute from the train object"""
        try:
            return train.origin.location[0].locationName
        except AttributeError:
            return ''
        
    def get_destination(self, train):
        """Extract the destination attribute from the train object"""
        try:
            return train.destination.location[0].locationName
        except AttributeError:
            return ''
    
    def get_platform(self, train):
        """Extract the platform attribute from the train object"""
        try:
            return train.platform
        except AttributeError:
            return ''
    
    def get_sch_dept(self, train):
        """Extract the scheduled departure time attribute from the train object"""
        try:
            return train.std
        except AttributeError:
            return ''
    
    def get_calling_stops(self, train):
        """Extract the calling stops from the subsequentCallingPoints 
           attributes of the object"""
        try:
            calling_stops = []
            stops = train.subsequentCallingPoints
            stop_list = stops.callingPointList[0][0]
            for stop in stop_list:
                calling_stops.append(calling_stop(stop.locationName,
                                                stop.st, stop.et))
            return calling_stops
        except AttributeError:
            return []
    

if __name__ == '__main__' :
    with open('token.txt', 'r') as csv_file:
        key = csv_file.read()
    board = service_board(key)
    services = board.get_services('VIC', 10)
    for service in services:
        print(services[service], '\n')
    

