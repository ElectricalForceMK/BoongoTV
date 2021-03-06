#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# 2014 - Anonymous
import base64
def decode(string):
    import base64
    s = ''
    str = _reverse(string)
    for x in range(0,len(str)):
        s += _decode_char(str[x])
    return base64.b64decode(s)
    
def _reverse(s):
    string = ''
    length = len(s)-3
    while length > 2:
        string += s[length]
        length = length - 1
    length = len(string)
    num2 = int(s[1]+s[0])/2
    if num2 < length:
        i = num2
        while i < length:
            if len(string) <= i: return string
            if (i+1) < length: string = string[0:i] + string[i+1:]
            i += num2
    return string
    
def _decode_char(c):
    array1 = ["0", "1", "2", "3", "4", "5", "6", "7", "9", "H", "M", "D", "X", "V", "J", "Q", "U", "G", "E", "T", "N", "o", "v", "y", "w", "k"]
    array2 = ["c", "I", "W", "m", "8", "L", "l", "g", "R", "B", "a", "u", "s", "p", "z", "Z", "e", "d", "=", "x", "Y", "t", "n", "f", "b", "i"]
    for i in range(0,len(array1)):
        if c == array1[i]: return array2[i][0]
        if c == array2[i]: return array1[i][0]
    return c


def decode_hls(file_url):
    def K12K(a, typ='b'):
        codec_a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'W', 'G', 'X', 'M', 'H', 'R', 'U', 'Z', 'I', 'D', '=', 'N', 'Q', 'V', 'B', 'L']
        codec_b = ['b', 'z', 'a', 'c', 'l', 'm', 'e', 'p', 's', 'J', 'x', 'd', 'f', 't', 'i', 'o', 'Y', 'k', 'n', 'g', 'r', 'y', 'T', 'w', 'u', 'v']
        if 'd' == typ:
            tmp = codec_a
            codec_a = codec_b
            codec_b = tmp
        idx = 0
        while idx < len(codec_a):
            a = a.replace(codec_a[idx], "___")
            a = a.replace(codec_b[idx], codec_a[idx])
            a = a.replace("___", codec_b[idx])
            idx += 1
        return a

    def _xc13(_arg1):
        _lg27 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        _local2 = ""
        _local3 = [0, 0, 0, 0]
        _local4 = [0, 0, 0]
        _local5 = 0
        while _local5 < len(_arg1):
            _local6 = 0
            while _local6 < 4 and (_local5 + _local6) < len(_arg1):
                _local3[_local6] = _lg27.find(_arg1[_local5 + _local6])
                _local6 += 1
            _local4[0] = ((_local3[0] << 2) + ((_local3[1] & 48) >> 4))
            _local4[1] = (((_local3[1] & 15) << 4) + ((_local3[2] & 60) >> 2))
            _local4[2] = (((_local3[2] & 3) << 6) + _local3[3])

            _local7 = 0
            while _local7 < len(_local4):
                if _local3[_local7 + 1] == 64:
                    break
                _local2 += chr(_local4[_local7])
                _local7 += 1
            _local5 += 4
        return _local2

    return _xc13(K12K(file_url, 'e'))

import re
def tr(param1 , param2 , param3):
    _loc4_ = 0;
    _loc5_= "";
    _loc6_ = None
    if( ord(param1[- 2]) == param2 and ord(param1[2]) == param3):
        _loc5_ = "";
        _loc4_ = len(param1)- 1;
        while(_loc4_ >= 0):
            _loc5_ = _loc5_ + param1[_loc4_]
            _loc4_-=1;
        param1 = _loc5_;
        _loc6_ = int(param1[-2:]);
        print 'xx',_loc6_
        param1 = param1[2:];
        param1 = param1[0:-3];
        _loc6_ = _loc6_ / 2;
        if(_loc6_ < len(param1)):
            _loc4_ = _loc6_;
        while(_loc4_ < len(param1)):
            param1 = param1[0:_loc4_]+ param1[_loc4_ + 1:]
            _loc4_ = _loc4_ + _loc6_ * 1;

        param1 = param1 + "!";

    return param1;

def swapme(st, fromstr , tostr):
    st=st.replace(tostr,"___")
    st=st.replace(fromstr,tostr)
    st=st.replace("___", fromstr)
    return st

     
def decode_sh(encstring):
    encstring=tr(encstring ,114,65)
    mc_from="MD7cXIZxt5B61RHbN8dovGzW3C"
    mc_to="myilk4UpJfYLgn0u9eQwsVaT2="
    if 1==2:#encstring.endswith("!"):
        encstring=encstring[:-1]
        mc_from="ngU08IuldVHosTmZz9kYL2bayE"
        mc_to="v7ec41D6GpBtXx3QJRiN5WwMf="

    st=encstring
    for i in range(0,len(mc_from)):
        st=swapme(st, mc_from[i], mc_to[i])
    print st
    return st.decode("base64")
    
