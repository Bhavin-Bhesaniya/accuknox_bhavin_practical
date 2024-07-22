# Use an official Ubuntu base image
FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    cowsay \
    fortune \
    netcat \
    && ln -s /usr/games/cowsay /usr/bin/cowsay \
    && ln -s /usr/games/fortune /usr/bin/fortune \
    && rm -rf /var/lib/apt/lists/*
    

# Set the working directory
WORKDIR /app

# Copy the shell script into the container
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Expose the application port
EXPOSE 4499

# Command to run the application
CMD ["/app/wisecow.sh"]
