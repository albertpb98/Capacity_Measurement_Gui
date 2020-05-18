clear all; %reseteamos todo ya que sino da error porque a (arduino) ya existe
a = arduino(); %creamos la coneixón con el arduino
addrs = string(scanI2CBus(a)); %buscamos su dirección
Sensor = device(a, 'I2CAddress', addrs); %creamos la conexión con el sensor a través del I2CAddress
reg0 = readRegister(Sensor, 0); %sin configurar nada más debería dar 7
writeRegister(Sensor,7,193); %193 es poner 1100 0001 en "Cap Setup", lo que queremos para activar el CIN2, el CAPCHOP y el ENABLE.
writeRegister(Sensor,9,11); %11 es poner 0000 1011 en el "EXC Setup".
writeRegister(Sensor,10,49) %49 es 0011 0001 para el Configurations (lo hemos visto en los registers del programa de AD)
writeRegister(Sensor,11,189); %189 es 1011 1101 para el CAP DAC A (lo hemos visto en los registers del programa de AD)
delay = 0.5;
mida = 500;

temps = -(mida*delay-delay) : delay : 0;
temps2 = -(mida*delay-delay) : delay : 0;

cap = zeros(1, mida);
capp = zeros(1, mida);

%de aquí en adelante obtenemos la información y la tratamos para facilitar su procesado

while 1
    
    cap1 = readRegister(Sensor, 1); %leemos los datos de capacidad de los registros correspondientes
    cap2 = readRegister(Sensor, 2);
    cap3 = readRegister(Sensor, 3);
    
    hexStr1 = dec2hex(cap1); %con tal de agruparlos en un string los convertimos a hex
    if(cap1<16) %necesitamos valores como: 8D, si da 07 únicamente dirá 7 y no podremos operar
        hexStr1 = ['0' hexStr1]; %añadimos el 0 al 07 para poder trabajar
    end
    hexStr2 = dec2hex(cap2);
    if(cap2<16)
        hexStr2 = ['0' hexStr2];
    end
    hexStr3 = dec2hex(cap3);
    if(cap3<16)
        hexStr3 = ['0' hexStr3];
    end
    
    yyaxis left 
    
    code = hex2dec([hexStr1 hexStr2 hexStr3]); %formamos el string total y lo convertimos a decimal para poder operar
    
    %Cin = (8*((code)/16777215)-4)*(0.000000000001); %operarmos con los valores en decimal, los normalizamos al dividir entre 16777215, multiplicamos por 8 y restamos 4 para que vaya de -4 a +4 y multiplicamos por 10-12 para que el valor sea en pF
    Cin = (5.85*((code)/16777215))*(1);
    %de aquí en adelante es el método usado para plotear las gráficas con AUTOSCALE
    
    cap(1:end-1) = cap(2:end); %Desplacem
    cap(end) = Cin; %Posem el valor al final
    
    temps(1:end-1)= temps(2:end); %Desplacem
    temps(end) = temps(end-1) + delay; %Afegim a la dreta
    
    plot(temps, cap);
   
    title('Capacitance measured')
    xlabel('Samples') 
    
   

    ylabel  ('Position (cm)') 
    
    yyaxis right 
    
   
    
    code2 = hex2dec([hexStr1 hexStr2 hexStr3]); %formamos el string total y lo convertimos a decimal para poder operar
    
    Cin2 = (8*((code)/16777215)-4)*(0.000000000001); %operarmos con los valores en decimal, los normalizamos al dividir entre 16777215, multiplicamos por 8 y restamos 4 para que vaya de -4 a +4 y multiplicamos por 10-12 para que el valor sea en pF
    %Cin2 = (5.85*((code)/16777215))*(1);
    %de aquí en adelante es el método usado para plotear las gráficas con AUTOSCALE
    
    capp(1:end-1) = capp(2:end); %Desplacem
    capp(end) = Cin2; %Posem el valor al final
    
    temps2(1:end-1)= temps2(2:end); %Desplacem
    temps2(end) = temps2(end-1) + delay; %Afegim a la dreta
    
    plot(temps2, capp);
    
    ylabel  ('Capacitance (f)') 
    
    
    drawnow
    
end