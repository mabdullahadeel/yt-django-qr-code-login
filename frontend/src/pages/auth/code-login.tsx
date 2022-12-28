import {
  Button,
  Flex,
  Heading,
  Spinner,
  useColorModeValue,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import React from "react";
import AuthRoute from "../../components/Authenticated/AuthRoute";
import { useCodeLoginWS } from "../../hooks/useCodeLoginWS";
import { authApi } from "../../services/authApi";
import { NextPageWithLayout } from "../../types/next.types";
import { APP_ORIGIN, queryKeys } from "../../utils/constants";
import QRCode from "react-qr-code";

const CodeLogin: NextPageWithLayout = () => {
  const { connect, error } = useCodeLoginWS();
  const { status, data, refetch } = useQuery(
    [queryKeys.GET_WS_KEY],
    authApi.getWsCode,
    {
      select: (data) => data.data,
      staleTime: 1000 * 60 * 9,
      onSuccess: async (data) => {
        try {
          await connect(data.ws_token);
        } catch (error) {
          console.log(error);
        }
      },
    }
  );

  return (
    <Flex height="100vh" alignItems="center" justifyContent="center">
      <Flex
        direction="column"
        alignItems="center"
        background={useColorModeValue("gray.100", "gray.700")}
        p={12}
        rounded={6}
      >
        <Heading mb={6}>Code Login</Heading>
        {status === "loading" && <Spinner />}
        {status === "success" && data && (
          <>
            <QRCode
              value={`${APP_ORIGIN}/quth/qr-login?code=${data.ws_token}`}
            />
            <Heading color="purple.300" mt={3}>
              {data.ws_token}
            </Heading>
          </>
        )}
        {status === "error" ||
          (error && (
            <>
              <Heading color="red">{error || "Error getting code"}</Heading>
              <Button colorScheme="red" onClick={() => refetch()}>
                Retry
              </Button>
            </>
          ))}
        <Link href="/auth/login">
          <Button width="100%" colorScheme="gray" variant="outline" mt={6}>
            Back
          </Button>
        </Link>
      </Flex>
    </Flex>
  );
};

CodeLogin.getLayout = (page) => {
  return <AuthRoute>{page}</AuthRoute>;
};

export default CodeLogin;
