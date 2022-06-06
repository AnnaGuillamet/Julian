# Julian
3D printer farm control

Expliació Projecte:
En la carpeta /src podem trobar:

  /enclosure
  
    /actuadors.py -- Hi trobarem les classes i funcions que retornaran l'acció aplicada per a controlar els valors d'incidencia.
    
    /sensors.py  -- Hi trobarem les classes i funcions que tractaran les dades obtingudes per MQTT i retornaran si hi ha alguna incidencia que es pugui resoldre    manualment o automaticament.
    
    /enclousure.py -- Hi trobarem la crida de sensors.py i actuadors.py, i també del script telegram.py, juntament amb aquestes crides gestionara els avisos via telegram i les mesures de control.
  
  /mqtt
  
    /randomData.py -- Script EXECUTABLE que ens proporcionara els valors aleatoris per a cada sensor i ho publicara al topic desitjat
    
    /subscribeData.py -- Script on ens subscriurem al topic i extraurem els valors dels sensors, i els tractarem amb el script importat enclosure.py
  
  /notificacions
  
    /channel.py -- Classe general dels canals on hi passarem el nostre token i chatId
    
    /telegram.py -- Script dedicat a establir la connexió amb el nostre bot i configurar algunes de les respostes i/o botons de telegram
    
  
  /julian.yaml -- Hi trobarem les dades de configuració
  
  /farm.py -- Hi trobarem la crida del script subscribeData.py i l'inicialitzarem
  
  /main.py -- Arxiu principal i EXECUTABLE, juntament amb el RandomData.py, on inicialitzara el projecte establint els valors de configuració. 
 
Terminal de sortida1: [executarem main.py]

Terminal de sortida2: [executarem randomData.py]

Obserarem que pel terminal de sortida1 s'imprimira:
"--Start Project Julian--" que ens informa del inici del programa
"--Configuration OK--" que ens informa de que s'ha carregat correctament la configuracio del julian.yaml
"--Start MQTT" que ens informa de s'iniciara la subscripcio al topic
"boot on the loop.." que ens informa que el bot esta corrent
Seguidament ens començara a sortir les frases "Result of treating the value [...]" que ens indicaran quin sensor esta tractant, el seu valor i l'acció que li pertoca. I, en alguns casos, la frase "--Control action applied:[...]" que ens indica si s'ha generat alguna acció de control. 
  
  
PD: Hola Miquel, 

Se que em vas recomanar que les dades obtingudes mitjançant MQTT, les tractes mitjançant una pila amb les commandes append() i pop(). He estat uns dies provant aquesta manera pero no me n'he sortit.. em fa rabia pero em sortien errors per culpa del 'loop_forever' que hi ha en mqtt, ja que mentres s'executava aquest loop la terminal es quedava parada sense poder realitzar el tractament de dades. 
