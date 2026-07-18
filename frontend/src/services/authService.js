import api from "../api/api";

export async function login(username, password) {

    const response = await api.post("/auth/login", {
        username,
        password,
    });

    localStorage.setItem(
        "token",
        response.data.access_token
    );

    return response.data;
}

export function logout() {

    localStorage.removeItem("token");

}

export function isAuthenticated() {

    return localStorage.getItem("token") !== null;

}