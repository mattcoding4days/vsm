# Maintainer: Matt Williams <matt.k.williams@protonmail.com>
pkgname="vsm"
pkgver=0.1.0
pkgrel=1
pkgdesc="A small python program for managing vim sessions"
arch=('x84_64')
url="https://github.com/mattcoding4days/vsm"
license=('GPL')
depends=("python>=3.10.1", "python-poetry>=1.1.12")
makedepends=("git")
source=("git+$url")

prepare() {
	cd "$pkgname-$pkgver"
	patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
}

build() {
	cd "$pkgname-$pkgver"
	./configure --prefix=/usr
	make
}

check() {
	cd "$pkgname-$pkgver"
	make -k check
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
