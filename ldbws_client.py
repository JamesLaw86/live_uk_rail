# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:46:34 2018

@author: James R Law
"""

from suds.sax.element import Element
from suds.client import Client

class idbws_client(object):
    """ 
    Makes SOAP requests to the Live Departure Boards Web Service 
    passes requests to a suds client member.
    Wraps all functions in the API
    
    """
    def __init__(self, key):
        """
        input - 'key' - your unique access token.
        """
        self.key = key
        self.url = 'https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01'
        self.namespace = ('ns2', 'http://thalesgroup.com/RTTI/2013-11-28/Token/types')
        self.header = Element('AccessToken', ns = namespace)
        header_val = Element('TokenValue', ns = namespace, parent = header)
        header_val.setText(key)
        self.header.append(header_val)
        self.__client = Client(self.url)
        self.__client.set_options(soapheaders = self.header)
        
    def get_departure_board(self, num_rows, crs,
                            filter_crs = None, 
                            filter_trs = None,
                            time_offset = None,
                            time_window = None):
        if not self.key:
            raise ValueError ('No access token set, request won\'t work!')
        
        return self.__client.service.GetDepartureBoard(num_rows, crs, filter_crs,
                                                filter_trs , time_offset,
                                                time_window)
                                                
        
#client = idbws_client(key)




