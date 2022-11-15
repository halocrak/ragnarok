import os
import requests
import user_agent
import random
logo='''
\033[31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠸⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⢸⠸⠀⡠⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⢠⣞⣀⡿⠀⠀⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡖⠁⠀⠀⠀⢸⠈⢈⡇⠀⢀⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠩⢠⡴⠀⠀⠀⠀⠀⠈⡶⠉⠀⠀⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠎⢠⣇⠏⠀⠀⠀⠀⠀⠀⠀⠁⠀⢀⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠏⠀⢸⣿⣴⠀⠀⠀⠀⠀⠀⣆⣀⢾⢟⠴⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⠀⠠⣄⠸⢹⣦⠀⠀⡄⠀⠀⢋⡟⠀⠀⠁⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡾⠁⢠⠀⣿⠃⠘⢹⣦⢠⣼⠀⠀⠉⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀
⠀⠀⢀⣴⠫⠤⣶⣿⢀⡏⠀⠀⠘⢸⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀
⠐⠿⢿⣿⣤⣴⣿⣣⢾⡄⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀
⠀⠀⠀⣨⣟⡍⠉⠚⠹⣇⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⢀⡀⣾⡇⠀⠀
⠀⠀⢠⠟⣹⣧⠃⠀⠀⢿⢻⡀⢄⠀⠀⠀⠀⠐⣦⡀⣸⣆⠀⣾⣧⣯⢻⠀⠀
⠀⠀⠘⣰⣿⣿⡄⡆⠀⠀⠀⠳⣼⢦⡘⣄⠀⠀⡟⡷⠃⠘⢶⣿⡎⠻⣆⠀⠀
⠀⠀⠀⡟⡿⢿⡿⠀⠀⠀⠀⠀⠙⠀⠻⢯⢷⣼⠁⠁⠀⠀⠀⠙⢿⡄⡈⢆⠀
⠀⠀⠀⠀⡇⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⠀⠀⠀⠀⠀⠀⡇⢹⢿⡀
⠀⠀⠀⠀⠁⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠇⠁
                CODY BY MRX
                FACBOOK : imfor x halo
                SNAPCHAT : mrx_coder
                TIKTOK : cvh1
                TELEGRAM CHANAL : @about_mrx'''
logo2='''
\033[32m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣀⣴⡯⠖⣓⣶⣶⡶⠶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢀⣴⣯⡾⣻⠽⡾⠽⠛⠚⠷⠯⠥⠤⠤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣢⣾⢿⣶⠿⣻⠿⠿⢋⣁⣠⠤⣶⢶⡆⠀⣀⣀⣀⣀⣀⣐⡻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠟⠛⠉⠪⠟⣩⠖⠋⢀⡴⢚⣭⠾⠟⠋⡹⣾⠀⠀⢀⣠⠤⠤⠬⠉⠛⠿⣷⡽⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⣿⢝⣯⠆⣩⠖⢀⣤⢞⣁⣄⣴⣫⡴⠛⠁⠀⡀⣼⠀⣿⢠⡴⠚⠋⠉⠭⠿⣷⣦⡤⢬⣝⣲⣌⡙⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⣷⣿⣿⣿⣿⠋⠀⢀⢀⣶⣷⣿⠀⣿⠀⠀⠀⠀⠀⠀⠐⠚⠻⣿⣶⣮⣛⢯⡙⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣸⣿⠋⠀⡆⣾⣾⣿⣿⠿⢂⣿⣄⠀⠀⠀⠀⠀⠀⠐⠢⢤⣉⢳⣍⠲⣮⣳⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠿⣷⡀⢸⣿⣿⣿⠙⠏⠁⣸⣿⣿⣭⣉⡁⠀⠀⠀⠀⠀⠀⠘⣿⣿⡷⣌⣿⡟⢿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡿⡏⢡⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣼⣿⡟⠋⠀⠀⣴⣿⣿⣦⣍⣙⣓⡦⠄⠀⠈⠙⠲⢦⣻⣿⡅⠘⣾⣿⡄⠹⡳⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢹⠀⠀⠞⢭⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠳⢼⣧⣄⣠⣾⣿⣿⣿⡻⢿⣭⡉⠁⠀⠀⠀⠀⠀⠀⠙⢿⢻⡄⠈⢻⣿⠀⠉⠹⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⡇⡆⠀⢀⣶⣾⣳⠏⠉⢹⡿⣿⣿⣟⡿⠿⢿⣿⣿⣿⣿⣧⠘⠒⠮⣿⣿⣿⣿⣿⣿⣿⣦⡬⠉⠀⠀⠀⢦⠀⠰⡀⠀⠈⠃⠓⠀⠈⣿⡀⠀⠀⢹⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣾⡧⣔⠾⡏⠙⠁⠀⣠⣿⢀⡎⠉⠈⠻⠭⠤⠤⣌⡻⣿⡿⡀⠈⠙⠻⠿⠿⣯⣅⠉⠉⣝⠛⢦⡘⣶⡀⠀⢣⠀⠙⢦⡀⠘⢇⣆⠀⣿⡇⠀⠀⠀⡇
⠀⠀⠀⠀⠀⣀⡠⠶⠿⠟⣃⣀⡀⠀⠀⠈⢓⣶⣾⣟⡡⠞⠀⠀⠀⠠⠴⠶⠿⠷⢿⡼⣿⣗⠀⠀⠀⠀⠀⠀⠈⠛⢆⠈⢧⡀⠁⠘⣿⡄⢢⠇⠀⠈⢧⠀⠸⣼⡄⣿⠇⠀⠀⢧⢸
⠀⣠⠴⠾⣿⡛⠛⠛⠁⠀⠀⠀⠙⠲⠈⠉⠀⠀⠀⠀⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠷⣄⠘⣷⣄⡀⡄⠀⢀⡀⠀⢳⡄⠀⠀⠳⠀⡏⠀⠀⠸⡄⠀⢿⣧⣿⠀⠀⠀⡀⣼
⣾⣿⢶⣦⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣤⣶⣶⣒⠢⢤⠀⠀⠈⠁⠉⠛⠿⣎⡛⢦⣀⠈⣿⣴⣾⣿⡞⡄⠀⠀⢹⡀⠀⠀⣿⠀⣾⣿⠇⠀⠀⠀⡇⢸
⠘⣿⣿⡾⡇⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡐⠲⢦⣦⢤⣤⣤⡶⠛⠉⠉⠀⠀⠀⠀⢀⣠⣤⣀⣤⠴⠂⠀⠀⠁⠀⢹⣧⣿⡿⢸⠇⢻⣿⣆⠀⠀⢷⣀⠀⣿⣷⠟⠉⠀⠀⠀⢸⡇⡄
⠀⠈⠳⢭⡗⠒⣛⣻⣽⠿⢿⣯⣷⣾⣿⣿⣿⣶⣬⡉⣉⠈⠑⠒⠉⠙⠻⠯⠉⣩⡟⢁⣾⠏⠀⣾⣷⣤⣄⣀⡀⢨⡿⣿⡇⣸⠀⠘⡿⢹⣆⠀⣸⣿⣷⡿⠁⠀⡀⠀⢸⡀⣾⣧⠀
⠀⠀⠀⠀⠈⠻⠿⣿⢿⡷⣌⣣⡉⠛⢿⣿⣿⣿⣿⣿⣧⡓⢄⠀⠀⠀⠀⠀⢰⡿⠷⣟⠿⠋⠀⢹⣿⡇⠀⠁⠙⣾⢧⠙⠙⠁⠀⠐⠁⠘⠹⣄⣿⠃⠹⣿⡀⠀⡇⠀⡿⣇⡿⢹⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⠻⠊⠙⠃⠀⠀⠹⣿⣿⡿⡏⠀⣿⣌⠳⡄⠀⢀⡴⠋⠈⠉⠉⡙⠲⣤⢸⡟⣿⠀⠀⠠⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠿⠃⠀⠀⠈⠃⣸⡇⣼⠇⣿⡇⢸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⢳⣿⣿⣿⡆⢳⠀⡎⠀⠀⠀⠀⢀⣉⠳⣬⣿⠇⠃⠀⠀⢠⠆⢰⢊⡇⠀⠀⠀⠀⠀⠀⢲⠀⢰⡆⠀⠀⣽⣿⡟⠀⢸⡇⡞⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢸⡇⠈⣿⢟⣼⣇⡏⠀⠀⠔⣺⡭⠽⣿⡛⠛⠿⡏⠀⣆⠀⠀⣼⠀⣼⣼⣷⡆⠀⠀⣶⡆⢠⡿⣠⣿⡇⠀⢰⣿⠏⣴⢂⠋⡼⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⢿⡁⣼⢣⣿⡿⠀⢀⢀⡴⠋⠀⠀⠀⠀⠙⣶⣦⡅⠀⣿⡄⢠⣿⣾⢿⠿⣿⡇⠀⠘⣾⣇⣼⣷⠟⡼⠀⣰⡿⠋⢠⠏⢦⣾⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡟⢾⢄⣹⣧⡿⡽⠁⠀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠟⠉⣧⡾⡽⣠⣿⢛⠇⠏⠰⣻⠃⣼⣽⣿⡿⡿⠁⣴⣡⡾⠋⠀⢠⣞⣴⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣼⣿⣿⡟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠋⠰⠟⣻⣿⢋⠀⠀⣴⣷⣾⠟⡿⠋⠀⣥⠾⠛⡋⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠽⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢁⡌⠀⢰⣿⠟⠁⠀⠀⠀⠀⡀⠀⣰⠃⠀⣴⡿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⢀⣴⠏⠀⠀⢸⡋⠀⡀⠀⣀⠖⠋⣠⣾⢃⣠⡾⠟⢡⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⣀⣴⡿⠃⠀⠀⠀⠀⢁⡾⠁⢈⣁⣴⣾⣿⣿⠟⠉⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣿⡿⠁⠀⢀⣀⣤⣼⢟⣡⣶⠿⠟⠋⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⣿⣿⣃⣴⣶⣿⠿⣿⣿⡿⠋⠀⠀⠀⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⣿⣿⣿⠛⠉⠀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠟⠁⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀
                                         CODY BY MRX
                                FACBOOK : imfor x halo
                                SNAPCHAT : mrx_coder
                                TIKTOK : cvh1
                                TELEGRAM CHANAL : @about_mrx⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
logo3='''
\033[34m

______  ___  _____  _   _   ___  ______ _____ _   __
| ___ \/ _ \|  __ \| \ | | / _ \ | ___ \  _  | | / /
| |_/ / /_\ \ |  \/|  \| |/ /_\ \| |_/ / | | | |/ / 
|    /|  _  | | __ | . ` ||  _  ||    /| | | |    \ 
| |\ \| | | | |_\ \| |\  || | | || |\ \\ \_/ / |\  
\_| \_\_| |_/\____/\_| \_/\_| |_/\_| \_|\___/\_| \_/
                                                    
                                                    

                                                                        
                                CODY BY MRX
                                FACBOOK : imfor x halo
                                SNAPCHAT : mrx_coder
                                TIKTOK : cvh1
                                TELEGRAM CHANAL : @about_mrx'''
class halo:
    def __init__(self):
        mrx =[logo,logo2,logo3]
        mrxhalo=random.choice(mrx)
        print(mrxhalo)
        print('1-MAKE WORD LIST NAME')
        print('2-DOMAIN TO IP')
        print('3-COMBO EMAIL')
        print('4-CHECK USER SNAPCHAT ')
        self.input()
    def input(self):
        halom=input('HALBZHERA :> ')
        if halom =='1':
            self.name()
        if halom =='2':
            self.domain()
        if halom =='3':
            self.email()
        if halom =='4':
            self.snap()
        else:
            input()
    def name(self):
        os.system('clear')
        mrx =[logo,logo2,logo3]
        mrxhalo=random.choice(mrx)
        print(mrxhalo)
        name=input("NAW : ")
        mr=range(10000)
        for i in mr:
            file=open("pass.txt","w")
            mrxm=requests.get(f"https://pass-list.halocrak.repl.co/name={name}").text
            print(mrx)
            file.write(f"{mrx} \n")
    def domain(self):
        os.system('clear')
        mrx =[logo,logo2,logo3]
        mrxhalo=random.choice(mrx)
        print(mrxhalo)
        name=input("DOMAIN : ")
        url=requests.get(f'https://domainip.halocrak.repl.co/domain={name}').text
        print(url)
    def email(self):
        os.system('clear')
        mrx =[logo,logo2,logo3]
        mrxhalo=random.choice(mrx)
        print(mrxhalo)
        os.system("rm -rif numcombo.txt")
        kkm = input("NAWEK BNWSA : ")
        qq =("@yahoo.com","@gmail.com","@hotmali.com")
        op=open("numcombo.txt","w")
        for x in range(100000000):
	        f = "1234567890"
	        x1 = random.choice(f)
	        x2 = random.choice(b)
	        x3 = random.choice(f)
	        x4 = random.choice(f)
	        x5 = random.choice(f)
	        x6 = random.choice(f)
	        x7 = random.choice(f)
	        x8 = random.choice(f)
	        x10 = random.choice(g)
	        x11 = random.choice(f)
	        x12 = random.choice(f)
	        x13 = random.choice(f)
	        x14 = random.choice(f)
	        x15 = random.choice(saz)
	        x16 = random.choice(qq)
	        dd = kkm+x1+x3+x4
	
	        jk = dd+x16+":"+dd
	        print(jk)
	        op.write(jk+"\n")
    def snap(self):
        os.system('clear')
        mrx =[logo,logo2,logo3]
        mrxhalo=random.choice(mrx)
        print(mrxhalo)
        name=input('USER SNAP CHAT : ')
        url=requests.get(f"https://snap-api.halocrak.repl.co/user={name}").text
        print(url)
	
	


        
