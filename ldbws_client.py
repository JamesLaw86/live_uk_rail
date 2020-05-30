# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:46:34 2018

@author: James R Law
"""

from suds.sax.element import Element
from suds.client import Client

class ldbws_client(object):
    """ 
    Makes SOAP requests to the Live Departure Boards Web Service 
    passes requests to a suds client member.
    Wraps all functions in the API.
    Doc strings copied directly from http://lite.realtime.nationalrail.co.uk/openldbws/?_ga=2.120914056.1808744076.1543671766-1118676336.1543671759
    
    """
    def __init__(self, key):
        """
        input - 'key' - your unique access token.
        """
        self.key = key
        self.url = 'https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01'
        self.namespace = ('ns2', 'http://thalesgroup.com/RTTI/2013-11-28/Token/types')
        self.header = Element('AccessToken', ns = self.namespace)
        header_val = Element('TokenValue', ns = self.namespace, parent = self.header)
        header_val.setText(key)
        self.header.append(header_val)
        self.__client = Client(self.url)
        self.__client.set_options(soapheaders = self.header)
        
    def get_departure_board(self, num_rows, crs,
                            filter_crs = None, 
                            filter_trs = None,
                            time_offset = None,
                            time_window = None):
        """Returns all public departures for the supplied CRS code
           within a defined time window."""
        return self.__client.service.GetDepartureBoard(num_rows, crs, filter_crs,
                                                       filter_trs , time_offset,
                                                       time_window)
        
    def get_dep_board_with_details(self, num_rows, crs,
                                   filter_crs = None, 
                                   filter_trs = None,
                                   time_offset = None,
                                   time_window = None):
        """Returns all public departures for the supplied CRS code
        within a defined time window, including service details."""
        return self.__client.service. GetDepBoardWithDetails(num_rows, crs, filter_crs,
                                                             filter_trs , time_offset,
                                                             time_window)
        
    def get_arrival_board(self,num_rows, crs,
                          filter_crs = None, 
                          filter_trs = None,
                          time_offset = None,
                          time_window = None):
        """Returns all public arrivals and departures for the
        supplied CRS code within a defined time window."""
        return self.__client.service.GetArrivalBoard(num_rows, crs, filter_crs,
                                                     filter_trs , time_offset,
                                                     time_window)
        
    def get_arr_board_with_details(self,num_rows, crs,
                                   filter_crs = None, 
                                   filter_trs = None,
                                   time_offset = None,
                                   time_window = None):
        """Returns all public arrivals and departures for the supplied CRS 
           code within a defined time window, including service details."""
        return self.__client.service.GetArrBoardWithDetails(num_rows, crs, filter_crs,
                                                     filter_trs , time_offset,
                                                     time_window)
        
    def get_arrival_departure_board(self,num_rows, crs,
                                    filter_crs = None, 
                                    filter_trs = None,
                                    time_offset = None,
                                    time_window = None):
        """Returns all public arrivals and departures for the supplied CRS
           code within a defined time window."""
        return self.__client.service.GetArrivalDepartureBoard(num_rows, crs, filter_crs,
                                                     filter_trs , time_offset,
                                                     time_window)
        
        
    def get_arr_dep_board_with_details(self,num_rows, crs,
                                       filter_crs = None, 
                                       filter_trs = None,
                                       time_offset = None,
                                       time_window = None):
        """Returns all public arrivals and departures for the supplied CRS
          code within a defined time window, including service details."""
        return self.__client.service. GetArrDepBoardWithDetails(num_rows, crs, filter_crs,
                                                     filter_trs , time_offset,
                                                     time_window)
        
        
    def get_next_departures(self, crs,
                            filter_list = None,
                            time_offset = None,
                            time_window = None):
        """Returns the next public departure for the supplied CRS 
        code withina defined time window to the locations specified
        in the filter."""
        return self.__client.service.GetNextDepartures(crs, filter_list,
                                                       time_offset, time_window)
    
    def get_next_departures_with_details(self, crs,
                                         filter_list = None,
                                         time_offset = None,
                                         time_window = None):
        """Returns the next public departure for the supplied CRS code
           within a defined time window to the locations specified in
           the filter, including service details."""
        return self.__client.service.GetNextDeparturesWithDetails(crs,
                                                                  filter_list,
                                                                  time_offset,
                                                                  time_window)
        
    def get_fastest_departures(self, crs,
                               filter_list = None,
                               time_offset = None,
                               time_window = None):
        """Returns the next public departure for the supplied CRS 
        code withina defined time window to the locations specified
        in the filter."""
        return self.__client.service.GetFastestDepartures(crs, filter_list,
                                                         time_offset, time_window)
        
    def get_fastest_departures_with_details(self, crs,
                                            filter_list = None,
                                            time_offset = None,
                                            time_window = None):
        """Returns the public departure for the supplied CRS code within a
        defined time window to the locations specified in the filter with
        the earliest arrival time at the filtered location, including
        service details."""
        return self.__client.service.GetFastestDeparturesWithDetails(crs,
                                                                     filter_list,
                                                                     time_offset,
                                                                     time_window)
        
        
    def get_service_details(self, str_serviceID):
        """Returns service details for a specific service identified by a
           station board. These details are supplied relative to the station
           board from which the serviceID field value was generated. Service
           details are only available while the service appears on the station
           board from which it was obtained. This is normally for two minutes
           after it is expected to have departed, or after a terminal arrival.
           If a request is made for a service that is no longer available
           then a null value is returned."""
        return self.__client.service.GetServiceDetails(str_serviceID)   
                                                
if __name__ == '__main__' :
    with open('token.txt', 'r') as csv_file:
        key = csv_file.read()
    client = ldbws_client(key)






