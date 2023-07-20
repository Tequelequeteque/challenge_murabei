'use client';
import { InputText } from 'primereact/inputtext';
import './styles.css';
import { Panel } from "primereact/panel";
import { Button } from 'primereact/button';
import { AutoComplete } from "primereact/autocomplete";
import { useCallback, useEffect, useRef, useState } from 'react';
import Api from '@/utils/api';
import { useRouter } from 'next/navigation';
import { InputNumber } from 'primereact/inputnumber';
import { Calendar } from 'primereact/calendar';
import { Toast } from 'primereact/toast';

export default function CreateBookPage() {
    const toast = useRef<Toast>(null);
    const router = useRouter();
    const [authors, setAuthors] = useState<any[]>([]);
    const [valueAuthor, setValueAuthor] = useState<any>('');
    const [selectedAuthor, setSelectedAuthor] = useState<any>(null);
    const [price, setPrice] = useState<any>();
    const [pubdate, setPubdate] = useState<Date>(new Date());
    const [pages, setPages] = useState<any>();

    const handleSubmit = useCallback((e: any) => {
        e.preventDefault();
        const data = {
            title: e.currentTarget.title.value,
            author: selectedAuthor.title,
            author_id: selectedAuthor.id,
            author_bio: selectedAuthor.biography,
            title_slug: e.currentTarget.slug_title.value,
            author_slug: selectedAuthor.slug,
            isbn13: e.currentTarget.isbn13.value,
            isbn10: e.currentTarget.isbn10.value,
            price: e.currentTarget.price.value,
            format: e.currentTarget.format.value,
            publisher: e.currentTarget.publisher.value,
            pubdate: pubdate.toJSON(),
            edition: e.currentTarget.edition.value,
            lexile: e.currentTarget.lexile.value,
            pages: pages,
            dimensions: e.currentTarget.dimensions.value,
            overview: e.currentTarget.overview.value,
            excerpt: e.currentTarget.excerpt.value,
            synopsis: e.currentTarget.synopsis.value,
            toc: e.currentTarget.toc.value,
            editorial_reviews: e.currentTarget.editorial_reviews.value,
        }
        Api.post('/books', data).then((book: any) => {
            toast.current?.show({ severity: 'success', summary: 'Criado com sucesso', life: 3000 });
            setTimeout(() => { router.push(`/books/${book.id}`) }, 3000);
        }).catch((e) => {
            console.error(e);
            toast.current?.show({ severity: 'error', summary: 'Erro ao criar', life: 3000 });
        })
    }, [selectedAuthor, pages, router, pubdate, toast]);

    const searchAuthors = useCallback(async () => {
        await Api.get<any[]>(`/authors?title=${valueAuthor}`)
            .then((data: any[]) => {
                setAuthors(data)
            })
            .catch(() => router.push('/login'));
    }, [valueAuthor, router]);

    useEffect(() => {
        searchAuthors();
    }, [searchAuthors]);

    return (<Panel header='Livros'>
        <form onSubmit={handleSubmit}>
            <Toast ref={toast}></Toast>
            <span className="p-float-label column">
                <InputText id="title" />
                <label htmlFor="title">Título</label>
            </span>
            <span className="p-float-label column">
                <InputText id="slug_title" />
                <label htmlFor="Título de Slug">Título de Slug</label>
            </span>
            <span className="p-float-label column">
                <InputText id="isbn13" />
                <label htmlFor="ISBN13">ISBN13</label>
            </span>
            <span className="p-float-label column">
                <InputText id="isbn10" />
                <label htmlFor="ISBN10">ISBN10</label>
            </span>
            <span className="p-float-label column">
                <InputNumber
                    inputId='price'
                    mode="currency"
                    currency="USD"
                    locale="en-US"
                    value={price}
                    onValueChange={(e) => setPrice(e.value)}
                />
                <label htmlFor="Preço">Preço</label>
            </span>
            <span className="p-float-label column">
                <InputText id="format" />
                <label htmlFor="Formato">Formato</label>
            </span>
            <span className="p-float-label column">
                <InputText id="publisher" />
                <label htmlFor="Editora">Editora</label>
            </span>
            <span className="p-float-label">
                <Calendar
                    inputId="pubdate"
                    value={pubdate}
                    onChange={(e: any) => setPubdate(e.value)}
                />
                <label htmlFor="Data de Publicação">Data de Publicação</label>
            </span>
            <span className="p-float-label column">
                <InputText id="edition" />
                <label htmlFor="Edição">Edição</label>
            </span>
            <span className="p-float-label column">
                <InputText id="lexile" />
                <label htmlFor="Lexile">Lexile</label>
            </span>
            <span className="p-float-label column">
                <InputNumber
                    inputId='pages'
                    value={pages}
                    onValueChange={(e) => setPages(e.value)}
                />
                <label htmlFor="Páginas">Páginas</label>
            </span>
            <span className="p-float-label column">
                <InputText id="dimensions" />
                <label htmlFor="Dimensões">Dimensões</label>
            </span>
            <span className="p-float-label column">
                <InputText id="overview" />
                <label htmlFor="Visão Geral">Visão Geral</label>
            </span>
            <span className="p-float-label column">
                <InputText id="excerpt" />
                <label htmlFor="Excerto">Excerto</label>
            </span>
            <span className="p-float-label column">
                <InputText id="synopsis" />
                <label htmlFor="Sinopse">Sinopse</label>
            </span>
            <span className="p-float-label column">
                <InputText id="toc" />
                <label htmlFor="Toc">Toc</label>
            </span>
            <span className="p-float-label column">
                <InputText id="editorial_reviews" />
                <label htmlFor="Revisões Editoriais">Revisões Editoriais</label>
            </span>
            <div className="column-full">
                <span className="p-float-label">
                    <AutoComplete
                        inputId="author"
                        completeMethod={searchAuthors}
                        value={valueAuthor}
                        onChange={(e) => setValueAuthor(e.value)}
                        onSelect={(e) => setSelectedAuthor(e.value)}
                        suggestions={authors}
                        name='author'
                        field='title'
                        dropdown
                        forceSelection={true}
                    />
                    <label htmlFor="Autor">Autor</label>
                </span>
            </div>
            <div className="column-full">
                <Button type='submit' label='Salvar' className='column' />
            </div>
        </form>
    </Panel>)
}