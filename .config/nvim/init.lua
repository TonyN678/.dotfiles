---@diagnostic disable: undefined-global

-- Set leader key
vim.g.mapleader = " "
vim.opt.termguicolors = true

-- ----------------------
-- LAZY PACKAGE MANAGER  |
-- ----------------------

-- This function check if there is a file called lazy.nvim already 
-- If not they will clone it and install
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)


-- add plugins to the neovim system through the lua/plugins directory
require("lazy").setup("plugins")

-- import vim options from vim-options.lua
require("vim-options")
-- import keymaps config from keymaps.lua
require("keymaps")
