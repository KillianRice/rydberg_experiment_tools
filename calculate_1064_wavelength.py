current_opo_wavelength = float(input('Current OPO Wavelength (cm^-1): '))
desired_opo_wavelength = float(input('Desired OPO Wavelength (cm^-1): '))
current_seed_wavelength =float( input('Current Seed Wavelength (nm): ') )

current_seed_wavenumber = 10**7/current_seed_wavelength
#print(current_seed_wavenumber)
desired_seed_wavenumber = desired_opo_wavelength - (current_opo_wavelength - current_seed_wavenumber)
#print(desired_seed_wavenumber)
desired_seed_wavelength = 1e7 / desired_seed_wavenumber

print('Set seed wavelength to: %4.3f nm'%desired_seed_wavelength)
input('Press Enter to Exit...')