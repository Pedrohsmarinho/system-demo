import axios from 'axios'

//criamos a url base do nosso projeto apos instanciar o axios
const axiosInstace = axios.create({
  baseURL:'http://localhost:3000'
})

export const api = {
  //metodos get
  get(endpoint){
    return axiosInstace.get(endpoint);
  },

  //metodos post
  post(endpoint,body){
    return axiosInstace.post(endpoint, body);
  },

  delete(endpoint){
    return axiosInstace.delete(endpoint)
  },

  put(endpoint,body){
    return axiosInstace.put(endpoint, body);
  }

}