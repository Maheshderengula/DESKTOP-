import React from 'react'
import Products from './Products/products';
import Login from './formEx/login';
import Reg from './reg';
const App = () => {
  return <div>
        <h3>App Component</h3>
        <Login/>
        <Reg/>
        <Products/> 
        </div>
}
export default App;