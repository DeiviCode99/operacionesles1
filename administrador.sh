
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
    read -p "Selecciona una opción [1-6]: " opcion
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
		    echo "========================================="
		    echo "       ESTADO DE MEMORIA Y DISCO"
		    echo "========================================="

		    echo "MEMORIA"
		    echo "-----------------------------------------"

		   # Memoria en GB
		    memoria_total=$(free -b | awk '/Mem:/ {
		        printf "%.1f", $2/1000000000
		    }')

		    memoria_usada=$(free -b | awk '/Mem:/ {
		        printf "%.1f", $3/1000000000
		    }')

		    memoria_disponible=$(free -b | awk '/Mem:/ {
		        printf "%.1f", $7/1000000000
		    }')

		    # Porcentaje de memoria utilizada
		    memoria_porcentaje=$(free | awk '/Mem:/ {
		        printf "%.0f", ($3/$2)*100
		    }')

		    echo "Memoria total: ${memoria_total} GB"
		    echo "Memoria utilizada: ${memoria_usada} GB"
		    echo "Memoria disponible: ${memoria_disponible} GB"
		    echo "Uso de memoria: ${memoria_porcentaje}%"

		    if [ "$memoria_porcentaje" -lt 85 ]; then
		        echo "Estado: OK"
		    else
		        echo "Estado: ADVERTENCIA"
		    fi

		    echo ""
		    echo "DISCO"
		    echo "-----------------------------------------"

		    # Disco en GB
		    disco_total=$(df -B1 / | awk 'NR==2 {
		        printf "%.1f", $2/1000000000
		    }')

		    disco_usado=$(df -B1 / | awk 'NR==2 {
		        printf "%.1f", $3/1000000000
		    }')

		    disco_disponible=$(df -B1 / | awk 'NR==2 {
		        printf "%.1f", $4/1000000000
		    }')

		    disco_porcentaje=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

		    echo "Sistema: /"
		    echo "Espacio total: ${disco_total} GB"
		    echo "Espacio utilizado: ${disco_usado} GB"
		    echo "Espacio disponible: ${disco_disponible} GB"
		    echo "Uso del disco: ${disco_porcentaje}%"

		    if [ "$disco_porcentaje" -lt 85 ]; then
		        echo "Estado: OK"
		    else
		        echo "Estado: ADVERTENCIA"
		    fi

		    echo ""
		    echo "SISTEMAS OPERACIONALES"
		    echo "INGENIERÍA DE SISTEMAS – UIS"
		    echo "2026-2"
		    echo "Diseñado por: Andrés Benavides Arévalo"

		    echo ""
		    read -p "Presione ENTER para continuar..."
		    ;;	  
	3)
	            while true; do
	                echo "========================================="
	                echo "       ADMINISTRACIÓN DE PROCESOS"
	                echo "========================================="
	                echo "1. Listar procesos activos"
	                echo "2. Buscar proceso por nombre"
	                echo "3. Mostrar procesos con mayor uso de CPU"
	                echo "0. Volver al menú principal"
	                echo "========================================="

	                read -p "Seleccione una opción: " proceso_opcion
	                echo ""

	                case $proceso_opcion in

	                    1)
	                        echo "========================================="
	                        echo "          PROCESOS ACTIVOS"
	                        echo "========================================="

	                        ps aux

	                        echo ""
	                        read -p "Presione ENTER para continuar..."
	                        ;;

	                    2)
	                        read -p "Ingrese el nombre del proceso: " nombre_proceso

	                        echo ""
	                        echo "Procesos encontrados:"
	                        echo "-----------------------------------------"

	                        ps aux | grep -i "$nombre_proceso" | grep -v grep

	                        echo ""
	                        read -p "Presione ENTER para continuar..."
	                        ;;

	                    3)
	                        echo "========================================="
	                        echo "    PROCESOS CON MAYOR USO DE CPU"
	                        echo "========================================="

	                        ps aux --sort=-%cpu | head -n 11

	                        echo ""
	                        read -p "Presione ENTER para continuar..."
	                        ;;

	                    0)
	                        break
	                        ;;

	                    *)
	                        echo "Opción no válida."
	                        read -p "Presione ENTER para continuar..."
	                        ;;

	                esac
	            done
	            ;;
	4)
		while true; do
		                echo "========================================="
		                echo "             INFORMACIÓN DE RED"
		                echo "========================================="
		                echo "1. Mostrar interfaces y direcciones IP"
		                echo "2. Mostrar puertos activos"
		                echo "3. Realizar prueba de conectividad"
		                echo "0. Volver"
		                echo "========================================="

		                read -p "Seleccione una opción: " red_opcion
		                echo ""

		                case $red_opcion in

		                    1)
		                        echo "========================================="
		                        echo "     INTERFACES Y DIRECCIONES IP"
		                        echo "========================================="

		                        ip a

		                        echo ""
		                        read -p "Presione ENTER para continuar..."
		                        ;;

		                    2)
		                        echo "========================================="
		                        echo "          PUERTOS ACTIVOS"
		                        echo "========================================="

		                        ss -tuln

		                        echo ""
		                        read -p "Presione ENTER para continuar..."
		                        ;;

		                    3)
		                        read -p "Ingrese el destino para la prueba [google.com]: " destino

		                        # Si el usuario no escribe nada, usa google.com
		                        if [ -z "$destino" ]; then
		                            destino="google.com"
		                        fi

		                        echo ""
		                        echo "Realizando prueba de conectividad hacia $destino..."
		                        echo "-----------------------------------------"

		                        ping -c 4 "$destino"

		                        echo ""
		                        read -p "Presione ENTER para continuar..."
		                        ;;

		                    0)
		                        break
		                        ;;

		                    *)
		                        echo "Opción no válida."
		                        read -p "Presione ENTER para continuar..."
		                        ;;

		                esac
		            done
		            ;;
	5)
	            echo "========================================="
	            echo "          BÚSQUEDA DE ARCHIVOS"
	            echo "========================================="

	            read -p "Ingrese el directorio inicial: " directorio
	            read -p "Ingrese el nombre o patrón: " patron

	            echo ""
	            echo "Buscando archivos..."
	            echo "-----------------------------------------"

	            # Verificar que el directorio exista
	            if [ ! -d "$directorio" ]; then
	                echo "Error: el directorio no existe."
	            else
	                resultados=$(find "$directorio" -type f -name "$patron" 2>/dev/null)

	                if [ -z "$resultados" ]; then
	                    echo "No se encontraron archivos."
	                    total=0
	                else
	                    echo "Resultados encontrados:"
	                    echo "$resultados"

	                    total=$(echo "$resultados" | wc -l)
	                fi

	                echo ""
	                echo "Total de archivos encontrados: $total"
	            fi

	            echo ""
	            echo "SISTEMAS OPERACIONALES"
	            echo "INGENIERÍA DE SISTEMAS – UIS"
	            echo "2026-2"
	            echo "Diseñado por: Andrés Benavides Arévalo"

	            echo ""
	            read -p "Presione ENTER para continuar..."
	            ;;
	6)
		    echo "========================================="
	            echo "          DIAGNÓSTICO DEL SISTEMA"
	            echo "========================================="
	            echo "Analizando recursos del sistema..."
	            echo ""

	            # -----------------------------------------
	            # DIAGNOSTICO DE MEMORIA
	            # -----------------------------------------
	            memoria_porcentaje=$(free | awk '/Mem:/ {
	                printf "%.0f", ($3/$2)*100
	            }')

	            if [ "$memoria_porcentaje" -lt 85 ]; then
	                echo "[OK] MEMORIA"
	                echo "Uso actual: $memoria_porcentaje%"
	                echo "La memoria se encuentra dentro de los límites establecidos."
	            else
	                echo "[ADVERTENCIA] MEMORIA"
	                echo "Uso actual: $memoria_porcentaje%"
	                echo "El uso de la memoria es superior al límite establecido: 85%."
	            fi

	            echo ""

	            # -----------------------------------------
	            # DIAGNOSTICO DE DISCO
	            # -----------------------------------------
	            disco_porcentaje=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

	            if [ "$disco_porcentaje" -le 85 ]; then
	                echo "[OK] DISCO"
	                echo "Uso actual: $disco_porcentaje%"
	                echo "El uso del disco se encuentra dentro de los límites establecidos."
	            else
	                echo "[ADVERTENCIA] DISCO"
	                echo "Uso actual: $disco_porcentaje%"
	                echo "El uso del disco es superior al límite establecido: 85%."
	            fi

	            echo ""

	            # -----------------------------------------
	            # DIAGNOSTICO DE RED
	            # -----------------------------------------
	            echo "Comprobando conectividad..."

	            if ping -c 2 -W 2 google.com > /dev/null 2>&1; then
	                echo "[OK] RED"
	                echo "Prueba de conectividad exitosa."
	                echo "Pérdida de paquetes: 0%."
	            else
	                echo "[ADVERTENCIA] RED"
	                echo "No fue posible realizar la prueba de conectividad."
	                echo "Verifique la conexión a Internet."
	            fi

	            echo ""

	            # -----------------------------------------
	            # DIAGNOSTICO DE PROCESOS
	            # -----------------------------------------
	            proceso_cpu=$(ps -eo pid,comm,%cpu --sort=-%cpu | sed -n '2p')

	            pid=$(echo "$proceso_cpu" | awk '{print $1}')
	            nombre=$(echo "$proceso_cpu" | awk '{print $2}')
	            cpu=$(echo "$proceso_cpu" | awk '{print $3}')

	            # Comparar uso de CPU
	            if awk "BEGIN {exit !($cpu > 80)}"; then
	                echo "[ADVERTENCIA] PROCESOS"
	                echo "Se detectó un proceso con alto consumo de CPU."
	                echo "Proceso:"
	                echo "PID: $pid"
	                echo "Nombre: $nombre"
	                echo "Uso de CPU: $cpu%"
	            else
	                echo "[OK] PROCESOS"
	                echo "No se detectaron procesos con consumo elevado de CPU."
	                echo "Proceso de mayor consumo:"
	                echo "PID: $pid"
	                echo "Nombre: $nombre"
	                echo "Uso de CPU: $cpu%"
	            fi

	            echo ""
	            echo "========================================="
	            echo "       DIAGNÓSTICO FINALIZADO"
	            echo "========================================="

	            read -p "Presione ENTER para continuar..."
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
