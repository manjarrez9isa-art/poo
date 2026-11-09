using System;

class HabitacionHotel
{
    // Atributos privados
    private int numero;
    private string tipo;
    private double precioPorNoche;
    private bool disponible;
    private string clienteActual;

    // Propiedades publicas
    public int Numero
    {
        get { return numero; }
    }

    public string Tipo
    {
        get { return tipo; }
        set
        {
            if (value == "Individual" ||
                value == "Doble" ||
                value == "Suite")
            {
                tipo = value;
            }
            else
            {
                throw new ArgumentException(
                    "Tipo de habitacion invalido.");
            }
        }
    }

    public double PrecioPorNoche
    {
        get { return precioPorNoche; }
        set
        {
            if (value > 0)
            {
                precioPorNoche = value;
            }
            else
            {
                throw new ArgumentException(
                    "El precio debe ser mayor a cero.");
            }
        }
    }

    public bool Disponible
    {
        get { return disponible; }
    }

    public string ClienteActual
    {
        get { return clienteActual; }
    }

    // Constructor
    public HabitacionHotel(
        int numero,
        string tipo,
        double precioPorNoche)
    {
        this.numero = numero;
        Tipo = tipo;
        PrecioPorNoche = precioPorNoche;
        disponible = true;
        clienteActual = "";
    }

    // Metodo Reservar
    public double Reservar(string nombreCliente, int noches)
    {
        if (disponible &&
            !string.IsNullOrWhiteSpace(nombreCliente) &&
            noches > 0)
        {
            disponible = false;
            clienteActual = nombreCliente;

            return precioPorNoche * noches;
        }

        return -1;
    }

    // Metodo Liberar
    public bool Liberar()
    {
        if (!disponible)
        {
            disponible = true;
            clienteActual = "";

            return true;
        }

        return false;
    }

    // Metodo MostrarInfo
    public string MostrarInfo()
    {
        string estado = disponible
            ? "Disponible"
            : "Ocupada";

        string cliente = disponible
            ? "Ninguno"
            : clienteActual;

        return "Habitacion: " + numero +
               "\nTipo: " + tipo +
               "\nPrecio por noche: $" +
               precioPorNoche.ToString("N0") +
               "\nEstado: " + estado +
               "\nCliente actual: " + cliente +
               "\n";
    }

    // Metodo AplicarDescuento
    public void AplicarDescuento(int porcentaje)
    {
        if (porcentaje >= 0 && porcentaje <= 100)
        {
            double nuevoPrecio = precioPorNoche *
                                 (1 - porcentaje / 100.0);

            if (nuevoPrecio > 0)
            {
                precioPorNoche = nuevoPrecio;
            }
            else
            {
                Console.WriteLine(
                    "El precio no puede ser cero o negativo.");
            }
        }
        else
        {
            Console.WriteLine(
                "Porcentaje de descuento invalido.");
        }
    }

    // Metodo ObtenerDatosResumen
    public string ObtenerDatosResumen()
    {
        string estado = disponible
            ? "Libre"
            : "Ocupada por: " + clienteActual;

        return "[" + numero + "] " +
               tipo + " - $" +
               precioPorNoche.ToString("N0") +
               " - " + estado;
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Crear las habitaciones
        HabitacionHotel h1 = new HabitacionHotel(
            101, "Individual", 55000);

        HabitacionHotel h2 = new HabitacionHotel(
            202, "Doble", 95000);

        HabitacionHotel h3 = new HabitacionHotel(
            303, "Suite", 300000);

        // Crear arreglo de habitaciones
        HabitacionHotel[] habitaciones = { h1, h2, h3 };

        // Mostrar estado inicial
        Console.WriteLine("================================");
        Console.WriteLine(" HOTEL ANJOY");
        Console.WriteLine("================================");

        Console.WriteLine("\n=== ESTADO INICIAL ===");

        Console.WriteLine(h1.MostrarInfo());
        Console.WriteLine(h2.MostrarInfo());
        Console.WriteLine(h3.MostrarInfo());

        // Reservas
        Console.WriteLine("=== RESERVAS ===");

        double costo1 = h1.Reservar(
            "Isai Manjarrez", 3);

        Console.WriteLine(
            "Reserva de Isai Manjarrez: $" +
            costo1.ToString("N0"));

        double costo2 = h2.Reservar(
            "Kevin Manjarrez", 2);

        Console.WriteLine(
            "Reserva de Kevin Manjarrez: $" +
            costo2.ToString("N0"));

        // Intentar reservar una habitacion ocupada
        double costo3 = h1.Reservar(
            "Frank Rincon", 2);

        if (costo3 == -1)
        {
            Console.WriteLine(
                "No se pudo reservar la habitacion 101.");
        }

        // Liberar habitacion 101
        bool liberada = h1.Liberar();

        Console.WriteLine(
            "¿Habitacion 101 liberada? " + liberada);

        // Aplicar descuento a la suite
        h3.AplicarDescuento(10);

        Console.WriteLine(
            "Nuevo precio de la suite: $" +
            h3.PrecioPorNoche.ToString("N0"));

        // Reservar nuevamente la habitacion 101
        double costo4 = h1.Reservar(
            "Yeleinis Cahuana", 1);

        Console.WriteLine(
            "Reserva de Yeleinis Cahuana: $" +
            costo4.ToString("N0"));

        // Mostrar estado final
        Console.WriteLine("\n=== ESTADO FINAL ===");

        Console.WriteLine(h1.MostrarInfo());
        Console.WriteLine(h2.MostrarInfo());
        Console.WriteLine(h3.MostrarInfo());

        // Mostrar resumen de habitaciones
        Console.WriteLine("\n=== RESUMEN DE HABITACIONES ===");

        foreach (HabitacionHotel habitacion in habitaciones)
        {
            Console.WriteLine(
                habitacion.ObtenerDatosResumen());
        }

        // Contar habitaciones libres y ocupadas
        int libres = 0;
        int ocupadas = 0;

        foreach (HabitacionHotel habitacion in habitaciones)
        {
            if (habitacion.Disponible)
            {
                libres++;
            }
            else
            {
                ocupadas++;
            }
        }

        Console.WriteLine("\n=== ESTADISTICAS DEL HOTEL ===");

        Console.WriteLine(
            "Habitaciones libres: " + libres);

        Console.WriteLine(
            "Habitaciones ocupadas: " + ocupadas);

        // Calcular precio promedio
        double sumaPrecios = 0;

        foreach (HabitacionHotel habitacion in habitaciones)
        {
            sumaPrecios += habitacion.PrecioPorNoche;
        }

        double promedio = sumaPrecios / habitaciones.Length;

        Console.WriteLine(
            "Precio promedio: $" +
            promedio.ToString("N0"));

        Console.WriteLine("\nPresione una tecla para salir...");
        Console.ReadKey();
    }
}
