from colorama import Fore, Back, Style, init

# Inicializar colorama (necesario en Windows, opcional en otros sistemas)
init()

# Usar colores en la consola
print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Back.YELLOW + "This has a yellow background")
print(Style.BRIGHT + "This text is bright")

# Restablecer los estilos al final
print(Style.RESET_ALL + "Back to normal text")
