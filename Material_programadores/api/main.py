#METODO GET DE HTTP
#EL NAVEGADOR TAMBIEN HACE PETICIONES
#importando la libreria

#import requests
#if __name__ == '__main__':
#    url = 'https://www.google.com.mx'
#    response=requests.get(url)#el metodo get retorna un objeto de tipo response
#    print(response)#EL VALOR 200 INDICA QUE LA PETICION SE REALIZO CORRECTAMENTE

#if response.status_code == 200:
#    content = response.content
#    file = open('google.html','wb')#wb write binary
#    file.write(content)
#    file.close()


#
import requests
if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {'nombre': 'Eduardo', 'curso': 'python', 'nivel': 'intermedio'}

    response = requests.get(url, params=args)
    if response.status_code == 200:
        content = response.content
        print(content)
