import { useState } from "react";
let Product=()=>{
    let [product,setProduct]=useState({"prod_Name":"Marker Pen", "price":30,qty:1})

    let incrHandler = ()=>{
        setProduct({...product, qty:product.qty+1})
    }
    let decrHandler = ()=>{
        setProduct({...product, qty:product.qty-1})
    }
    return <div>
            <h3>Produc component</h3>
            <h4>Product Name:{product.prod_Name}</h4>
            <h4>Price:{product.price}</h4>
            <h4>QTY:{product.qty}</h4>
            <button onClick={decrHandler}>-</button>
            <button onClick={incrHandler}>+</button>
            <h3>Total:{product.qty * product.price}</h3>
            </div>
}
export default Product;