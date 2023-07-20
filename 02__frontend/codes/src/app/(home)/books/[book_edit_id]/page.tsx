'use client'
import Api from "@/utils/api";
import './styles.css'
import { useRouter } from "next/navigation";
import { AutoComplete } from "primereact/autocomplete";
import { Button } from "primereact/button";
import { Calendar } from "primereact/calendar";
import { InputNumber } from "primereact/inputnumber";
import { InputText } from "primereact/inputtext";
import { Panel } from "primereact/panel";
import { Toast } from "primereact/toast";
import { useCallback, useEffect, useRef, useState } from "react";

export default function EditBookPage({ params: { book_edit_id } }: any) {
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
            title: e.currentTarget.title?.value,
            author: selectedAuthor.title,
            author_id: selectedAuthor.id,
            author_bio: selectedAuthor.biography,
            title_slug: e.currentTarget.title_slug.value,
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
        Api.put(`/books/${book_edit_id}`, data).then((book: any) => {
            toast.current?.show({ severity: 'success', summary: 'Editado com sucesso', life: 3000 });
        }).catch((e) => {
            console.error(e);
            toast.current?.show({ severity: 'error', summary: 'Erro ao editar', life: 3000 });
        })
    }, [selectedAuthor, pubdate, pages, toast, book_edit_id]);

    const searchAuthors = useCallback(async () => {
        await Api.get<any[]>(`/authors?title=${valueAuthor}`)
            .then((data: any[]) => {
                setAuthors(data)
            })
            .catch(() => router.push('/login'));
    }, [valueAuthor,router]);

    const [book, setBook] = useState<any>(null);
    const getBook = useCallback(async () => {
        await Api.get<any[]>(`/books`, {
            params: {
                id: book_edit_id
            }
        }).then((data: any) => {
            setBook(data)
            setPrice(data.price.replace('$', ''))
            setPubdate(new Date(data.pubdate))
            setPages(data.pages)
            setValueAuthor(data.author_rel)
            setSelectedAuthor(data.author_rel)
        })
            .catch(() => router.push('/login'));
    }, [book_edit_id,router]);

    useEffect(() => {
        getBook();
        searchAuthors();
    }, [getBook,searchAuthors]);
    if (!book) { return <i className="pi pi-spin pi-cog" style={{ fontSize: '2rem' }}></i> }

    return (<Panel header='Livros'>
        <form onSubmit={handleSubmit}>
            <Toast ref={toast}></Toast>
            <span className="p-float-label column">
                <InputText id="title" defaultValue={book?.title} />
                <label htmlFor="title">Título</label>
            </span>
            <span className="p-float-label column">
                <InputText id="title_slug" defaultValue={book?.title_slug} />
                <label htmlFor="Título de Slug">Título de Slug</label>
            </span>
            <span className="p-float-label column">
                <InputText id="isbn13" defaultValue={book?.isbn13} />
                <label htmlFor="ISBN13">ISBN13</label>
            </span>
            <span className="p-float-label column">
                <InputText id="isbn10" defaultValue={book?.isbn10} />
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
                <InputText id="format" defaultValue={book?.format} />
                <label htmlFor="Formato">Formato</label>
            </span>
            <span className="p-float-label column">
                <InputText id="publisher" defaultValue={book?.publisher} />
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
                <InputText id="edition" defaultValue={book?.edition} />
                <label htmlFor="Edição">Edição</label>
            </span>
            <span className="p-float-label column">
                <InputText id="lexile" defaultValue={book?.lexile} />
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
                <InputText id="dimensions" defaultValue={book?.dimensions} />
                <label htmlFor="Dimensões">Dimensões</label>
            </span>
            <span className="p-float-label column">
                <InputText id="overview" defaultValue={book?.overview} />
                <label htmlFor="Visão Geral">Visão Geral</label>
            </span>
            <span className="p-float-label column">
                <InputText id="excerpt" defaultValue={book?.excerpt} />
                <label htmlFor="Excerto">Excerto</label>
            </span>
            <span className="p-float-label column">
                <InputText id="synopsis" defaultValue={book?.synopsis} />
                <label htmlFor="Sinopse">Sinopse</label>
            </span>
            <span className="p-float-label column">
                <InputText id="toc" defaultValue={book?.toc} />
                <label htmlFor="Toc">Toc</label>
            </span>
            <span className="p-float-label column">
                <InputText id="editorial_reviews" defaultValue={book?.editorial_reviews} />
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