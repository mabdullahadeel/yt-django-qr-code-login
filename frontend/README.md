# React Token Auth Template

> This reposity is a template for a React app that uses token authentication.
> Initially, it was created to be used with django and django-rest-framework, but it can be used with any backend that uses token authentication.

## How to use

You can clone the repository and start working on it, or you can use it as a template for your own repository.

## How to run

Since, it's a nextjs app, you can run it with the following commands:

```bash
yarn install
yarn dev
```

## Tech Stack

- Nextjs
- React
- Chakra UI
- Axios
- React Query
- React Hook Form
- Typescript

## Features

1. All the core logic for authentication and token handling lives in the [TokenAuthContext](./src/context/TokenAuthContext.tsx) file. All necessory functions are exported from there and are available through the [useAuth](./src/hooks/useAuth.ts) hook.
2. The [LoginForm](./src/pages/auth/login.tsx) and [RegisterForm](./src/pages/auth/register.tsx) components are already setup to use the [useAuth](./src/hooks/useAuth.ts) hook. You can use them as is, or you can create your own components.
3. Forms are validated using [react-hook-form](https://react-hook-form.com/).
4. Tokens are stored in the browser's local storage.
5. [axios](https://axios-http.com/) is used for making requests to the backend. The defult url for local development is `http://localhost:8000`. You can change it in the [constants.ts](./src/utils/constants.ts) file.
6. [Chakra UI](https://chakra-ui.com/) is used for styling. You can change the theme in the [theme.ts](./src/theme/theme.ts) file.
