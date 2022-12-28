import React from "react";
import { Button, Center, Heading, Stack, Text } from "@chakra-ui/react";
import Link from "next/link";

interface HomePageProps {}

export const HomePageContent: React.FC<HomePageProps> = () => {
  return (
    <Center>
      <Stack>
        <Heading>Welcome</Heading>
        <Text>You are logged in</Text>
        <Link href="auth/qr-login">
          <Button variant="solid" colorScheme="red">
            Login with Code
          </Button>
        </Link>
      </Stack>
    </Center>
  );
};
