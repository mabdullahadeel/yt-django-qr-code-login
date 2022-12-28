import React from "react";
import { Center, Heading, Stack, Text } from "@chakra-ui/react";

interface HomePageProps {}

export const HomePageContent: React.FC<HomePageProps> = () => {
  return (
    <Center>
      <Stack>
        <Heading>Welcome</Heading>
        <Text>You are logged in</Text>
      </Stack>
    </Center>
  );
};
