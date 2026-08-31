import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from scripts import funciones

# ── Colores del tema Catppuccin Mocha ──
BG_PRINCIPAL = "#1e1e2e"
BG_LATERAL   = "#181825"
BG_INPUT     = "#313244"
BG_BOTON     = "#313244"
BG_BOTON_ACT = "#89b4fa"
TEXTO        = "#cdd6f4"
TEXTO_SEC    = "#a6adc8"
ACENTO       = "#f38ba8"
VERDE        = "#a6e3a1"
BORDES       = "#45475a"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binary Representation")
        self.geometry("900x550")
        self.configure(bg=BG_PRINCIPAL)
        self.resizable(False, False)

        self.opcion_actual = None

        self.crear_panel_lateral()
        self.crear_area_principal()

        self.mostrar_opcion(1)

    # ──────────────────────────────────────────────
    #  PANEL LATERAL
    # ──────────────────────────────────────────────
    def crear_panel_lateral(self):
        self.lateral = tk.Frame(self, bg=BG_LATERAL, width=200)
        self.lateral.pack(side="left", fill="y")
        self.lateral.pack_propagate(False)

        titulo = tk.Label(self.lateral, text="Binary\nRep.",
                          bg=BG_LATERAL, fg=TEXTO,
                          font=("Segoe UI", 18, "bold"))
        titulo.pack(pady=(30, 40))

        opciones = [
            ("1", "Decimal->Binario"),
            ("2", "Tabla ASCII"),
            ("3", "Analizar Doc."),
            ("4", "Binary Detective"),
        ]

        self.botones = []
        for num, texto in opciones:
            btn = tk.Button(self.lateral, text=f" {num}  {texto}",
                            bg=BG_BOTON, fg=TEXTO,
                            font=("Segoe UI", 11),
                            bd=0, anchor="w", padx=15, pady=10,
                            activebackground=BG_BOTON_ACT,
                            activeforeground=BG_PRINCIPAL,
                            cursor="hand2",
                            command=lambda n=num: self.mostrar_opcion(n))
            btn.pack(fill="x", padx=10, pady=3)
            self.botones.append((num, btn))

    # ──────────────────────────────────────────────
    #  AREA PRINCIPAL
    # ──────────────────────────────────────────────
    def crear_area_principal(self):
        self.area = tk.Frame(self, bg=BG_PRINCIPAL)
        self.area.pack(side="right", fill="both", expand=True)

        self.panel1 = self.crear_panel_conversion()
        self.panel2 = self.crear_panel_ascii()
        self.panel3 = self.crear_panel_documento()
        self.panel4 = self.crear_panel_detective()

    def mostrar_opcion(self, num):
        for panel in [self.panel1, self.panel2, self.panel3, self.panel4]:
            panel.pack_forget()

        for boton_num, btn in self.botones:
            if boton_num == str(num):
                btn.configure(bg=BG_BOTON_ACT)
            else:
                btn.configure(bg=BG_BOTON)

        clave = str(num)
        paneles = {"1": self.panel1, "2": self.panel2,
                   "3": self.panel3, "4": self.panel4}
        paneles[clave].pack(fill="both", expand=True, padx=20, pady=20)
        self.opcion_actual = clave

    # ──────────────────────────────────────────────
    #  PANEL 1: DECIMAL A BINARIO
    # ──────────────────────────────────────────────
    def crear_panel_conversion(self):
        panel = tk.Frame(self.area, bg=BG_PRINCIPAL)

        tk.Label(panel, text="Decimal a Binario",
                 bg=BG_PRINCIPAL, fg=TEXTO,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 15))

        frame_input = tk.Frame(panel, bg=BG_PRINCIPAL)
        frame_input.pack(fill="x", pady=(0, 10))

        tk.Label(frame_input, text="Numero decimal:",
                 bg=BG_PRINCIPAL, fg=TEXTO_SEC,
                 font=("Segoe UI", 11)).pack(anchor="w")

        self.entry_numero = tk.Entry(frame_input, bg=BG_INPUT, fg=TEXTO,
                                     insertbackground=TEXTO, font=("Consolas", 13),
                                     bd=0, highlightthickness=1,
                                     highlightbackground=BORDES)
        self.entry_numero.pack(fill="x", ipady=8)
        self.entry_numero.bind("<Return>", lambda e: self.convertir())

        tk.Button(panel, text="Convertir",
                  bg=BG_BOTON_ACT, fg=BG_PRINCIPAL,
                  font=("Segoe UI", 11, "bold"),
                  bd=0, cursor="hand2", padx=20, pady=8,
                  command=self.convertir).pack(anchor="w", pady=(0, 15))

        self.resultado_conversion = tk.Text(panel, bg=BG_INPUT, fg=TEXTO,
                                            font=("Consolas", 12), bd=0,
                                            highlightthickness=1,
                                            highlightbackground=BORDES,
                                            height=10, state="disabled")
        self.resultado_conversion.pack(fill="both", expand=True)

        return panel

    def convertir(self):
        texto = self.entry_numero.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Ingrese un numero")
            return
        try:
            numero = int(texto)
            resultado = funciones.convert_to_binary(numero)
            self.resultado_conversion.configure(state="normal")
            self.resultado_conversion.delete("1.0", "end")
            self.resultado_conversion.insert("1.0", resultado)
            self.resultado_conversion.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un numero valido")

    # ──────────────────────────────────────────────
    #  PANEL 2: TABLA ASCII
    # ──────────────────────────────────────────────
    def crear_panel_ascii(self):
        panel = tk.Frame(self.area, bg=BG_PRINCIPAL)

        tk.Label(panel, text="Tabla ASCII",
                 bg=BG_PRINCIPAL, fg=TEXTO,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 15))

        frame_input = tk.Frame(panel, bg=BG_PRINCIPAL)
        frame_input.pack(fill="x", pady=(0, 10))

        tk.Label(frame_input, text="Texto a analizar:",
                 bg=BG_PRINCIPAL, fg=TEXTO_SEC,
                 font=("Segoe UI", 11)).pack(anchor="w")

        self.entry_texto = tk.Entry(frame_input, bg=BG_INPUT, fg=TEXTO,
                                    insertbackground=TEXTO, font=("Consolas", 13),
                                    bd=0, highlightthickness=1,
                                    highlightbackground=BORDES)
        self.entry_texto.pack(fill="x", ipady=8)
        self.entry_texto.bind("<Return>", lambda e: self.generar_ascii())

        tk.Button(panel, text="Generar tabla",
                  bg=BG_BOTON_ACT, fg=BG_PRINCIPAL,
                  font=("Segoe UI", 11, "bold"),
                  bd=0, cursor="hand2", padx=20, pady=8,
                  command=self.generar_ascii).pack(anchor="w", pady=(0, 15))

        # Treeview (tabla)
        columnas = ("caract", "decimal", "hex", "binario")
        self.tabla_ascii = ttk.Treeview(panel, columns=columnas,
                                        show="headings", height=10)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background=BG_INPUT, foreground=TEXTO,
                        fieldbackground=BG_INPUT, font=("Consolas", 11),
                        rowheight=28)
        style.configure("Treeview.Heading",
                        background=BG_BOTON, foreground=TEXTO,
                        font=("Segoe UI", 10, "bold"))

        self.tabla_ascii.heading("caract", text="Caracter")
        self.tabla_ascii.heading("decimal", text="Decimal")
        self.tabla_ascii.heading("hex", text="Hex")
        self.tabla_ascii.heading("binario", text="Binario")

        self.tabla_ascii.column("caract", width=80, anchor="center")
        self.tabla_ascii.column("decimal", width=100, anchor="center")
        self.tabla_ascii.column("hex", width=100, anchor="center")
        self.tabla_ascii.column("binario", width=150, anchor="center")

        self.tabla_ascii.pack(fill="both", expand=True)

        self.info_tamanio = tk.Label(panel, text="",
                                     bg=BG_PRINCIPAL, fg=ACENTO,
                                     font=("Segoe UI", 10))
        self.info_tamanio.pack(anchor="w", pady=(10, 0))

        return panel

    def generar_ascii(self):
        texto = self.entry_texto.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Ingrese un texto")
            return

        for item in self.tabla_ascii.get_children():
            self.tabla_ascii.delete(item)

        for char in texto:
            dec = ord(char)
            hex_val = format(dec, 'x')
            bin_val = format(dec, 'b')
            self.tabla_ascii.insert("", "end", values=(char, dec, hex_val, bin_val))

        bytes_tam = len(texto.encode('UTF-8'))
        self.info_tamanio.configure(
            text=f"Tamano: {bytes_tam} bytes | {bytes_tam * 8} bits")

    # ──────────────────────────────────────────────
    #  PANEL 3: ANALIZAR DOCUMENTO
    # ──────────────────────────────────────────────
    def crear_panel_documento(self):
        panel = tk.Frame(self.area, bg=BG_PRINCIPAL)

        tk.Label(panel, text="Analizar Documento",
                 bg=BG_PRINCIPAL, fg=TEXTO,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 15))

        # Frame para ruta y boton examinar
        frame_ruta = tk.Frame(panel, bg=BG_PRINCIPAL)
        frame_ruta.pack(fill="x", pady=(0, 10))

        tk.Label(frame_ruta, text="Ruta del documento:",
                 bg=BG_PRINCIPAL, fg=TEXTO_SEC,
                 font=("Segoe UI", 11)).pack(anchor="w")

        frame_ruta_input = tk.Frame(frame_ruta, bg=BG_PRINCIPAL)
        frame_ruta_input.pack(fill="x")

        self.entry_ruta_doc = tk.Entry(frame_ruta_input, bg=BG_INPUT, fg=TEXTO,
                                       insertbackground=TEXTO, font=("Consolas", 12),
                                       bd=0, highlightthickness=1,
                                       highlightbackground=BORDES)
        self.entry_ruta_doc.pack(side="left", fill="x", expand=True, ipady=8)

        tk.Button(frame_ruta_input, text="Examinar",
                  bg=BG_BOTON, fg=TEXTO,
                  font=("Segoe UI", 10),
                  bd=0, cursor="hand2", padx=12, pady=6,
                  command=self.examinar_documento).pack(side="right", padx=(8, 0))

        # Boton analizar
        tk.Button(panel, text="Analizar",
                  bg=VERDE, fg=BG_PRINCIPAL,
                  font=("Segoe UI", 11, "bold"),
                  bd=0, cursor="hand2", padx=20, pady=8,
                  command=self.analizar_documento).pack(anchor="w", pady=(0, 15))

        # Area de resultado
        self.resultado_documento = tk.Text(panel, bg=BG_INPUT, fg=TEXTO,
                                           font=("Consolas", 12), bd=0,
                                           highlightthickness=1,
                                           highlightbackground=BORDES,
                                           height=12, state="disabled")
        self.resultado_documento.pack(fill="both", expand=True)

        return panel

    def examinar_documento(self):
        ruta = filedialog.askopenfilename(title="Selecciona un documento")
        if ruta:
            self.entry_ruta_doc.delete(0, "end")
            self.entry_ruta_doc.insert(0, ruta)

    def analizar_documento(self):
        ruta = self.entry_ruta_doc.get().strip()
        if not ruta:
            messagebox.showwarning("Aviso", "Seleccione un documento primero")
            return
        try:
            with open(ruta, 'rb') as f:
                contenido = f.read()

            nombre = ruta.split('/')[-1].split('\\')[-1]
            tamano = len(contenido)

            # Verificar si es texto plano
            try:
                texto_contenido = contenido.decode('UTF-8')
                es_texto = True
            except UnicodeDecodeError:
                es_texto = False

            resultado = f"Archivo: {nombre}\n"
            resultado += f"Tamano: {tamano} bytes\n"
            resultado += f"Tipo: {'Texto plano' if es_texto else 'Binario'}\n"
            resultado += f"Ruta: {ruta}\n"

            if es_texto:
                preview = texto_contenido[:500]
                if len(texto_contenido) > 500:
                    preview += "\n... (vista previa cortada en 500 caracteres)"
                resultado += f"\n--- Vista previa ---\n{preview}"
            else:
                hex_preview = contenido[:32].hex()
                hex_preview = " ".join([hex_preview[i:i+2] for i in range(0, len(hex_preview), 2)])
                resultado += f"\n--- Primeros bytes (hex) ---\n{hex_preview.upper()}"

            self.resultado_documento.configure(state="normal")
            self.resultado_documento.delete("1.0", "end")
            self.resultado_documento.insert("1.0", resultado)
            self.resultado_documento.configure(state="disabled")

        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo no encontrado")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo analizar: {e}")

    # ──────────────────────────────────────────────
    #  PANEL 4: BINARY DETECTIVE
    # ──────────────────────────────────────────────
    def crear_panel_detective(self):
        panel = tk.Frame(self.area, bg=BG_PRINCIPAL)

        tk.Label(panel, text="Binary Detective",
                 bg=BG_PRINCIPAL, fg=TEXTO,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 5))

        tk.Label(panel, text="Detecta el tipo real de un archivo por sus magic numbers",
                 bg=BG_PRINCIPAL, fg=TEXTO_SEC,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(0, 15))

        # Boton seleccionar archivo
        frame_botones = tk.Frame(panel, bg=BG_PRINCIPAL)
        frame_botones.pack(fill="x", pady=(0, 15))

        tk.Button(frame_botones, text="Seleccionar archivo...",
                  bg=BG_BOTON_ACT, fg=BG_PRINCIPAL,
                  font=("Segoe UI", 11, "bold"),
                  bd=0, cursor="hand2", padx=20, pady=8,
                  command=self.ejecutar_detective).pack(anchor="w")

        # Label de estado
        self.estado_detective = tk.Label(panel, text="Esperando seleccion de archivo...",
                                         bg=BG_PRINCIPAL, fg=TEXTO_SEC,
                                         font=("Segoe UI", 10))
        self.estado_detective.pack(anchor="w", pady=(0, 10))

        # Area de resultado
        self.resultado_detective = tk.Text(panel, bg=BG_INPUT, fg=TEXTO,
                                           font=("Consolas", 11), bd=0,
                                           highlightthickness=1,
                                           highlightbackground=BORDES,
                                           height=14, state="disabled")
        self.resultado_detective.pack(fill="both", expand=True)

        return panel

    def ejecutar_detective(self):
        ruta = filedialog.askopenfilename(title="Selecciona el archivo a analizar")
        if not ruta:
            return

        self.estado_detective.configure(text=f"Analizando: {ruta.split('/')[-1].split('\\')[-1]}...",
                                        fg=ACENTO)
        self.update()

        try:
            resultado = funciones.detective(ruta)

            self.resultado_detective.configure(state="normal")
            self.resultado_detective.delete("1.0", "end")
            self.resultado_detective.insert("1.0", resultado)
            self.resultado_detective.configure(state="disabled")

            self.estado_detective.configure(text="Analisis completado", fg=VERDE)

        except Exception as e:
            self.estado_detective.configure(text="Error al analizar", fg=ACENTO)
            messagebox.showerror("Error", f"No se pudo analizar el archivo:\n{e}")
