# TestSprite Next.js Demo

A simple Next.js application built to test TestSprite features including:
- Authentication flows (login/logout with test credentials)
- Form validation and submission (contact form)
- API routes (GET and POST endpoints)
- Protected pages (dashboard requires auth)
- Navigation and routing
- Error handling and 404 pages

## Test Credentials
- Email: `test@example.com`
- Password: `password123`

## Getting Started

First, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Pages
- `/` - Home page with feature list
- `/about` - About page
- `/contact` - Contact form (posts to API)
- `/login` - Login page (use test credentials above)
- `/dashboard` - Protected page (requires login)

## API Routes
- `GET /api/hello` - Returns a hello message
- `POST /api/contact` - Accepts contact form data
