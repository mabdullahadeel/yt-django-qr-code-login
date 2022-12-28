import "../styles/globals.css";
import type { AppProps } from "next/app";
import { AuthConsumer, AuthProvider } from "../context/TokenAuthContext";
import { NextPageWithLayout } from "../types/next.types";
import { AbsoluteCenter, Box, ChakraProvider, Spinner } from "@chakra-ui/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import Head from "next/head";

const client = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 300,
    },
  },
});

interface MyAppProps extends AppProps {
  Component: NextPageWithLayout;
}

function MyApp(props: MyAppProps) {
  const { Component, pageProps } = props;
  const getLayout = Component.getLayout || ((page) => page);

  return (
    <>
      <Head>
        <title>Next Token Auth</title>
      </Head>
      <ChakraProvider>
        <QueryClientProvider client={client}>
          <AuthProvider>
            <AuthConsumer>
              {(auth) =>
                !auth.isInitialized ? (
                  <Box h="100vh">
                    <AbsoluteCenter>
                      <Spinner />
                    </AbsoluteCenter>
                  </Box>
                ) : (
                  getLayout(<Component {...pageProps} />)
                )
              }
            </AuthConsumer>
          </AuthProvider>
          <ReactQueryDevtools position="bottom-right" initialIsOpen={false} />
        </QueryClientProvider>
      </ChakraProvider>
    </>
  );
}

export default MyApp;
