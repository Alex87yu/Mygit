#!/usr/bin/env python3
# -*- coding: utf-8 -*-

bpd=6.8
ac=21.5
fl=4.9
bdp=float(input('请输入bdp:厘米'))
ac=float(input('请输入ac:厘米'))
fl=float(input('请输入fl:厘米'))
weight=1.07*bpd*bpd*bpd+0.3*ac*ac*fl 
print('宝宝的体重是%.2f克'%weight)
