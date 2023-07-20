
import axios from 'axios'
export default class Api {
    private static axios = axios.create({
        baseURL: process.env.API_URL,
        headers: {
            'no-cache': 'true',
        }
    })

    static _init() {
        this.axios.interceptors.request.use((config) => {
            const token = localStorage.getItem('library_token')
            if (token) {
                config.headers.Authorization = `Bearer ${token}`
            }
            return config
        })
    }

    static async get<T>(url: string, config: any = undefined): Promise<T> {
        return this.axios.get(url, config).then((res) => res.data)
    }

    static async post<T>(url: string, body: any, config: any = undefined): Promise<T> {
        return this.axios.post(url, body, config).then((res) => res.data)
    }

    static async put<T>(url: string, body: any, config: any = undefined): Promise<T> {
        return this.axios.put(url, body, config).then((res) => res.data)
    }

    static async delete<T>(url: string, config: any = undefined): Promise<T> {
        return this.axios.delete(url, config).then((res) => res.data)
    }
}

Api._init()