import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'

const Products = () => {
    let [products, setProducts] = useState([])
    let [loading, setLoading] = useState(true)
    let [error, setError] = useState(null)

    useEffect(()=>{
        Axios.get('https://dummyjson.com/products')
            .then((resp)=>{
                setProducts(resp.data.products || [])
                setLoading(false)
            })
            .catch((err)=>{
                setError(err.message)
                setLoading(false)
            })
    },[])
    
    if (loading) return <div className="container mt-5"><p>Loading...</p></div>
    if (error) return <div className="container mt-5"><p className="text-danger">Error: {error}</p></div>

    return (
        <div className="container mt-5">
            <h2 className="mb-4">Products</h2>
            <table className="table table-striped table-hover">
                <thead className="table-dark">
                    <tr>
                        <th>Product Id</th>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Category</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product) => (
                        <tr key={product.id}>
                            <td>{product.id}</td>
                            <td>{product.title}</td>
                            <td>${product.price}</td>
                            <td>{product.category}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Products