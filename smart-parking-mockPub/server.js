const http = require("http");
const express = require("express");
const app = express();
const cors = require("cors");

app.use(cors());

app.get("/dadosSobreVagas", function(req, res) {
    res.json(
        {
            "vagas":[
              {"id": 1,"situacao": "ocupada"},
              {"id": 2,"situacao": "ocupada"},
              {"id": 3,"situacao": "livre"},
              {"id": 4,"situacao": "livre"},
              {"id": 5,"situacao": "livre"},
              {"id": 6,"situacao": "ocupada"},
              {"id": 7,"situacao": "ocupada"},
              {"id": 8,"situacao": "livre"},
              {"id": 9,"situacao": "livre"},
              {"id": 10,"situacao": "ocupada"},
              {"id": 11,"situacao": "livre"}
            ],
            "vagaslivres": 20,
            "vagasOcupadas": 39,
              "localDoEstacionamento": "Shopping North Way",
              "dataDeAtualizacao": "20/12/2022",
              "horaDeAtualizacao": "23:44:44",
          }
    );
});

http.createServer(app).listen(3000, () => console.log("Servidor rodando local na porta 3000"));