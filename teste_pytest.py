import requests

class TestCursos:
    headers = {'Authorization': 'Token 921a9b2afb5e60c7c1b513ad4e5ee8de33d9909c'}
    url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
    
    def test_get_cursos(self):
        cursos = requests.get(url=self.url_cursos, headers=self.headers)
        assert cursos.status_code == 200
    
    def test_get_curso(self):
        resposta = requests.get(url=f"{self.url_cursos}15/", headers=self.headers)
        assert resposta.status_code == 200
        
    def test_post_curso(self):
        novo = {
            "titulo": "Api é legal!", 
            "url": "http://www.bduhvb.com.brrr"
            }
        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo["titulo"]
    
    def test_put_curso(self):
        atualizado = {
            "titulo": "Api é legal1", 
            "url": "http://www.bduhvb.com.brr"
            }
        resposta = requests.put(url=f'{self.url_cursos}15/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
    
    def test_put_titulo(self):
        atualizado = {
            "titulo": "Api é legal1", 
            "url": "http://www.bduhvb.com.brr"
            }
        resposta = requests.put(url=f'{self.url_cursos}15/', headers=self.headers, data=atualizado)
        assert resposta.json()['titulo'] == atualizado['titulo']
    
    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_cursos}15/', headers=self.headers)
        assert resposta.status_code == 204 and len (resposta.text) == 0
        