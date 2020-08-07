import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

const loadTweets = (callbk) => {
  const xhr = new XMLHttpRequest();
  const method = 'GET';
  const url = "http://localhost:8001/api/tweets";
  const responseType = "json";

  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.onload = () => {
      callbk(xhr.response, xhr.status)
  }
  xhr.onerror = function(e){
    console.log(e);
    callbk({"message": "The request was an error"}, 400)
  }
  xhr.send();
}


/******Like Button Element*****/
const ActionBtn = props =>{
  const {tweet, action} = props;
  const className = props.className ? props.className : 'btn btn-primary btn-sm';
  return action.type == 'like' ? <button className={className}>{tweet.likes} Like</button> : null;
};

function Tweet(props){
  const {tweet} = props;
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6 bg-secondary';
  return <div className={className}>
    <p>{tweet.content}</p>
    <div className='btn btn-group'>
      <ActionBtn tweet={tweet} action={{type: 'like'}} />
    </div>
  </div>
}

function App() {
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    const myCallback = (res, stat) => {
      if(stat === 200){
        setTweets(res)
      } else {
        alert("There was an error!")
      }
    }
    loadTweets(myCallback);
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {tweets.map((tweet, i) => <Tweet tweet={tweet} key={i} />)}
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
