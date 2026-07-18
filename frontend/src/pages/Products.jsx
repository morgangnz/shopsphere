import { useEffect, useState } from "react";
import { getProducts } from "../services/productService";

function Products() {

    const [products, setProducts] = useState([]);

    useEffect(() => {

        async function loadProducts() {

            const data = await getProducts();

            setProducts(data);

        }

        loadProducts();

    }, []);

    return (

        <div style={{ padding: 40 }}>

            <h1>Productos</h1>

            <table border="1" cellPadding="10">

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>Nombre</th>

                        <th>Precio</th>

                        <th>Stock</th>

                    </tr>

                </thead>

                <tbody>

                    {products.map(product => (

                        <tr key={product.id}>

                            <td>{product.id}</td>

                            <td>{product.name}</td>

                            <td>{product.price}</td>

                            <td>{product.stock}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default Products;