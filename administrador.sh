
#!/bin/bash
#Bucle para el menu
while true; do
    echo "========================================="
    echo "       SMART LINUX SYSTEM MONITOR"
    echo "              Autor: Andres"
    echo "========================================="
    echo "1. Información general del sistema"
    echo "2. Estado de memoria y disco"
    echo "3. Administración de procesos"
    echo "4. Información y prueba de red"
    echo "5. Buscar archivos"
    echo "6. Generar diagnóstico del sistema"
    echo "0. Salir"
    echo "========================================="
    read -p "Selecciona una opción [1-4]: " opcion
    echo ""
    case $opcion in 
	1)
		echo -n "Usuario actual: "
		whoami
		echo -n "DIrectorio actual: "
		pwd
		echo -n "nombre del equipo: "
		hostname
		echo  "Sistema operativo"
		lsb_release -ds
		echo  "Arquitectura"
		uname -m
		echo "Fecha y hora"
		date
		read -p "Presione Enter para continuar..."
		;;
	2)
		echo ""
		;;
	3)
		;;
	4)
		;;
	5)
		;;
	6)
		;;
	0)
		echo "Saliendo..."
		exit 0
		;;
	*)
		echo "Opcion no valida"
		read -p "Presione enter para continuar..."
		;;
   esac
done
