public static class JuegoPalabras
{
    public static void Run()
    {
        Random rnd = new Random();

        int randomNumber = rnd.Next(1, 101);

        Console.WriteLine("¡Bienvenido al juego de adivinar el número!");

        int trys = 0;
        bool guessed = false;

        while (!guessed)
        {
            int input;

            while (true)
            {
                Console.Write("Introduce un número entre 1 y 100: ");

                if (int.TryParse(Console.ReadLine(), out input))
                    break;

                Console.WriteLine("Ingrese un número entero: ");
            }

            trys++;
            if (input == randomNumber)
            {
                Console.WriteLine("Has adivinado el número!");
                Console.WriteLine($"Número de intentos: {trys}");
                guessed = true;
            }

            else
            {
                Console.WriteLine("Intenta de nuevo.");
                Hint(input, randomNumber);
            }
        }
    }
    private static void Hint(int input, int randomNumber)
    {
        if (input > randomNumber)
        {
            Console.WriteLine("El número ingresado es mayor.");
        }
        else
        {
            Console.WriteLine("El número ingresado es menor.");
        }
    }
}

