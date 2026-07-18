import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Products from "./pages/Products";
import Dashboard from "./pages/Dashboard";
import Categories from "./pages/Categories";

import Navbar from "./components/Navbar";
import PrivateRoute from "./components/PrivateRoute";

function App() {

    return (

        <Routes>

            <Route
                path="/"
                element={<Login />}
            />

            <Route
                path="/products"
                element={
                    <PrivateRoute>
                        <>
                            <Navbar />
                            <Products />
                        </>
                    </PrivateRoute>
                }
            />

            <Route
                path="/categories"
                element={
                    <PrivateRoute>
                        <>
                            <Navbar />
                            <Categories />
                        </>
                    </PrivateRoute>
                }
            />

            <Route
                path="/dashboard"
                element={
                    <PrivateRoute>
                        <>
                            <Navbar />
                            <Dashboard />
                        </>
                    </PrivateRoute>
                }
            />

        </Routes>

    );

}

export default App;