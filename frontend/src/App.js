import axios from "axios";
import React from "react";

class App extends React.Component {
    state = {
        details: [],
    }

    componentDidMount() {
    debugger
        let data;
        axios.get('http://localhost:8000/api')
          .then(res => {
            data=res.data
            this.setState(
              {details: data}
            )
          })
          .catch(err => {
            console.log(err);
          })
      }

    render () {
        debugger
        return (
            <div>
                <header>Данные из Django</header>
                <hr></hr>
                {this.state.details.map((output, id)=>{
                  return <div key={id}>
                    <div>
                      <h2>{output.title}</h2>
                      <p>{output.description}</p>
                    </div>
                  </div>
                })}
            </div>
          );
    }
}

export default App;
