import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json
import time
from samp_client.client import SampClient
from datetime import datetime
from datetime import timedelta
import pytz
from discord.ext import tasks
import threading
import asyncio
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!') #Prefijo del bot

import os
contenido = os.listdir('.')
print(contenido)
    
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Haciendo Kimikoz"))
    print("Bot is ready!")
    
@bot.command(name='h') #Funcion que dice la hora Colombia
async def hora(ctx):
    hora=time.strftime("%I:%M:%S %p")
    response = ("La hora donde yo vivo: ")+hora
    await ctx.send(response)

@bot.command(name='calendario') #Envia imagen
async def calendario(ctx):
    await ctx.send(file=discord.File('./calendario.jpeg'))

@bot.command(name='s') #Funcion que realizara la suma entre dos numeros enteros
async def sumar(ctx, num1,num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

@bot.command(name='m') #Funcion que realizara la multi entre dos 
async def multiplicar(ctx, num1,num2):
    response = int(num1)*int(num2)
    await ctx.send(response)

@bot.command(name='on') #Funcion conocer jugadores conectados FZ S4
async def jugadores_on(ctx):
    with SampClient(address='158.69.175.161', port=7777) as client:
        ls=(client.get_server_info())
    response="Jugadores conectados en "+ls[3]+" : "+str(ls[1])
    await ctx.send(response)

@bot.command(name='entregas') #Funcion conocer cuanto tiempo falta de entregas
async def entregas(ctx):
    timeZ_Colombia = pytz.timezone('America/Bogota')
    dateZ_Colombia = datetime.now (timeZ_Colombia)
    hora_Co= dateZ_Colombia.strftime("%H:%M:%S")
    fecha_Co= dateZ_Colombia.strftime("%Y-%m-%d %H:%M:%S")
    numero_entregas=16
    fecha_Referencia = ("2022-04-02 17:00:00")
    i=0
    lista_Entregas=[]
    lista_Restante=[]
    lista_Encargados=[
                      "Ryan_Hyztherls",
                      "Gabriel_Vasseur",
                      "Treizy_Varkell",
                      "Helena_Harper",
                      "Method_Wutang",
                      "Asher_Westwod",
                      "Francesca_Sokolova",
                      "Quenzy_Hertz",
                      "Hans_Yerkov",
                      "Camilo_Arenas",
                      "Noel_Soto",
                      "Anthony_Lobo",
                      "Ryan_Hyztherls",
                      "Dimi_Tryggxz"
                      ]
    fecha_Tipificada=datetime.strptime(fecha_Referencia, "%Y-%m-%d %H:%M:%S")
    o=0
    for e in range (numero_entregas):
        fecha=fecha_Tipificada + timedelta(days=2)
        lista_Entregas.append(fecha)
        fecha_Tipificada=fecha_Tipificada + timedelta(days=2)
        o=o+1
    
    o=0
    for e in range (numero_entregas):
        if fecha_Co <= (lista_Entregas[e].strftime("%Y-%m-%d %H:%M:%S")):
            fecha_Co=datetime.strptime(fecha_Co, "%Y-%m-%d %H:%M:%S")
            diferencia=lista_Entregas[e]-fecha_Co
            break
        o=o+1
    try:
        response=("Las siguientes entregas serán en **"+ str(diferencia) +" Horas**"+"\n"+"`Encargado/a: "+lista_Encargados[o]+"`")
    except:
        response=("No sé, hay que preguntarle a Brian Loro")
    await ctx.send(response)
    

@tasks.loop(seconds=1, count=1)
async def mensaje(response):
    channel = await bot.fetch_channel(661965426246549517) #channel id here
    #channel = await bot.fetch_channel(913601944600322131)
    await channel.send(response)
      
    
    
def revisar_fecha():
    print("Revisando fecha entregas")
    response=""
    while -1:
        if (len(response) > 0):
            mensaje.start(response)
            response=""
        timeZ_Colombia = pytz.timezone('America/Bogota')
        dateZ_Colombia = datetime.now (timeZ_Colombia)
        hora_Co= dateZ_Colombia.strftime("%H:%M:%S")
        fecha_Co= dateZ_Colombia.strftime("%Y-%m-%d %H:%M:%S")
        numero_entregas=16
        fecha_Referencia = ("2022-04-02 17:00:00")
        i=0
        lista_Entregas=[]
        lista_Restante=[]
        lista_Encargados=[
                      "Ryan_Hyztherls",
                      "Gabriel_Vasseur",
                      "Treizy_Varkell",
                      "Helena_Harper",
                      "Method_Wutang",
                      "Asher_Westwod",
                      "Francesca_Sokolova",
                      "Quenzy_Hertz",
                      "Hans_Yerkov",
                      "Camilo_Arenas",
                      "Noel_Soto",
                      "Anthony_Lobo",
                      "Ryan_Hyztherls",
                      "Dimi_Tryggxz"]
        fecha_Tipificada=datetime.strptime(fecha_Referencia, "%Y-%m-%d %H:%M:%S")
        for e in range (numero_entregas):
            fecha=fecha_Tipificada + timedelta(days=2)
            lista_Entregas.append(fecha)
            fecha_Tipificada=fecha_Tipificada + timedelta(days=2)     
        o=0
        for e in range (numero_entregas):
            if ((dateZ_Colombia.strftime("%Y-%m-%d %H:%M")) == (lista_Entregas[e].strftime("%Y-%m-%d %H:%M"))):
                try:
                    response=("@everyone @here Entregas en **15m**"+"\n"+"`Encargado/a: "+lista_Encargados[o]+"`")
                except:
                    response=""
                break 
            o=o+1
        time.sleep(60)

def arranque_bot():
    bot.run(TOKEN)

        
            
#hilo1 = threading.Thread(target=arranque_bot)
#hilo1.start()
async def bot_async_start():
    await bot.start(TOKEN)


def bot_loop_start(loop):
    loop.run_forever()


def bot_start():
    loop = asyncio.get_event_loop()
    loop.create_task(bot_async_start())
    bot_thread = threading.Thread(target=bot_loop_start, args=(loop,))
    bot_thread.start()
    
bot_start()
revisar_fecha()






