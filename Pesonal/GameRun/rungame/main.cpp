#include<SDL.h>
#include<string>
#include <SDL_image.h>



class player
{
    int hp=100,dame=10,ki=20;

};
int main(int argc, char* args[]) {
    SDL_Window* window = SDL_CreateWindow("My SDL Window", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 800, 600, SDL_WINDOW_SHOWN);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    SDL_Surface* imageSurface = IMG_Load("assets/Player/run/row-1-column-1.png");
    if (imageSurface == NULL) {
        fprintf(stderr, "Image loading failed: %s\n", IMG_GetError());
        return 1;
    }

    SDL_Texture* imageTexture = SDL_CreateTextureFromSurface(renderer, imageSurface);
    SDL_FreeSurface(imageSurface);
    SDL_Surface* resizeimg = SDL_CreateRGBSurface(0, 100, 100, imageTexture->format->BitsPerPixel,imageTexture ->format->Rmask, imageTexture->format->Gmask, imageTexture->format->Bmask,imageTexture ->format->Amask);
    bool quit = false;//run
    SDL_Event e;
    while (!quit) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }
        }

        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, imageTexture, NULL, NULL);
        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
